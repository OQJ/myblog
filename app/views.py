from app import app
from flask import render_template, redirect, url_for, flash, session
from app.model import Tag, Post, Admin
from app.forms import TagForm, PostForm, DeleteForm, LoginForm
from app.model import db
from flask_login import login_user, logout_user , current_user, login_required


@app.route('/')
def index():
    posts = Post.query.order_by(Post.create_time.desc()).all()
    form = DeleteForm()

    return render_template('index.html', posts=posts, form=form)


@app.route('/tag_list', methods=['GET', 'POST'])
def tag():
    form = TagForm()
    tags = Tag.query.all()
    if form.validate_on_submit():
        name = form.name.data
        tag = Tag(name=name)
        db.session.add(tag)
        db.session.commit()
        flash('create success!', 'success')
        return redirect(url_for('tag'))
    return render_template('tag_list.html', form=form, tags=tags)


@app.route('/del_tag/<int:id>')
@login_required
def del_tag(id):
    tag = Tag.query.get_or_404(id)
    db.session.delete(tag)
    db.session.commit()
    flash('delect success!', 'success')
    return redirect(url_for('tag'))


@app.route('/edit_tag/<int:id>')
@login_required
def edit_tag(id):
    form = TagForm()
    tag = Tag.query.get_or_404(id)
    form.name.data = tag.name
    if form.validate_on_submit():
        pass
    return render_template('tag_edit.html', form=form)


@app.route('/new_post', methods=['POST', 'GET'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        tag = int(form.tag.data)
        post = Post(title=title, body=body, tag_id=tag)
        db.session.add(post)
        db.session.commit()
        flash('创建成功', 'success')
        return redirect(url_for('index'))

    return render_template('new_post.html', form=form)


@app.route('/edit_post/<int:id>', methods=['POST', 'GET'])
@login_required
def edit_post(id):
    post = Post.query.get_or_404(id)
    form = PostForm()
    
    form.title.data = post.title
    form.body.data = post.body
    form.tag.data = post.tag_id
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        tag = int(form.tag.data)
        post = Post(title=title, body=body, tag_id=tag)
        db.session.add(post)
        db.session.commit()
        flash('创建成功', 'success')
        return redirect(url_for('index'))

    return render_template('edit_post.html',form=form, post=post)

@app.route('/detail_post/<int:id>')
def detail_post(id):
   
    post = Post.query.get_or_404(id)
    return render_template('detail_post.html', post=post)

@app.route('/delete_post', methods=['POST'])
@login_required
def delete_post():
    form = DeleteForm()
    id = form.id.data
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('删除成功', 'success')
    return redirect(url_for('index'))
    

@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(name=form.user_name.data).first()
        if user and user.check_password_hash(form.password.data):
            login_user(user)
            flash('登陆成功', 'success')
            from app.utils import redirect_back
            return redirect_back()
        else:
            flash('登录失败')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('退出成功', 'success')
    return redirect(url_for('index'))