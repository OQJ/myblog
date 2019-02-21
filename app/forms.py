from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField, PasswordField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired, ValidationError, Length
from app.model import Tag, Admin


class TagForm(FlaskForm):
    name = StringField('名字',validators=[DataRequired()], render_kw={'class':'text '})
    submit = SubmitField('提交', render_kw={'class':'btn btn-primary '})

    def validate_name(self,field):
        if Tag.query.filter_by(name=field.data).first():
            raise ValidationError('标签已经存在')

class PostForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired()], render_kw={'class':' from-control col-md-5 '})
    body = CKEditorField('内容', validators=[DataRequired()])
    tag = SelectField('主题', coerce=int, default=1)
    submit = SubmitField('发布')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.tag.choices = [(tag.id, tag.name) for tag in Tag.query.order_by(Tag.name).all() ]


class DeleteForm(FlaskForm):
    id = HiddenField('id', validators=[DataRequired()])
    submit = SubmitField('删除')


class LoginForm(FlaskForm):
    user_name = StringField('用户名', validators=[DataRequired()], render_kw={'required':'required'})
    password = PasswordField('密码', validators=[DataRequired()], render_kw={'required':'required'})
    submit = SubmitField('Login')

    def validate_usr_name(self, field):
        if not Admin.query.filter_by(name=field.data).first():
            raise ValidationError('用户名或者密码错误')




























