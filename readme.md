# 项目结构

在本模板中，根目录是`flask-template`，下面有几个重要的文件夹和文件：

- `app/`：该文件夹包含应用程序的主要代码。
  - `static/`：静态文件夹，用于存放 CSS、JavaScript 和图像文件。
    - `css/`：存放 CSS 文件的文件夹。
    - `js/`：存放 JavaScript 文件的文件夹。
    - `img/`：存放图像文件的文件夹。
  - `templates/`：存放 HTML 模板文件的文件夹。
    - `model.html`：基础模板，其他页面模板可以继承它。
    - `index.html`：示例主页模板，可以添加其他页面模板。
  - `__init__.py`：应用程序的初始化文件，包含创建 Flask 应用程序对象的代码。
  - `models.py`：包含使用 Flask-SQLAlchemy 定义的数据库模型。
  - `routes.py`：包含应用程序的路由和视图函数。
  - `func.py`: 包含应用程序调用的函数。

- `migrations/`：用于数据库迁移的文件夹，使用 Flask-Migrate 和 Alembic 管理数据库模式变更。
  - `versions/`：存放数据库迁移脚本的文件夹。
  - `alembic.ini`：Alembic 配置文件。
  - `env.py`：Alembic 环境配置文件。
  - `script.py.mako`：Alembic 脚本生成模板。

- `.database/`：用于数据库文件的文件夹。
  - `data.sqlite`：SQlite文件，用于储存数据。

- `config.py`：包含应用程序的配置参数，例如数据库连接信息、密钥等。

- `requirements.txt`：列出项目所需的所有依赖包及其版本。

- `run.py`：用于启动应用程序的脚本。

- `virtualdata.py`: 用于生成虚拟数据库数据，发布调试。

请注意，这只是一种组织结构示例，您可以根据自己的项目需求进行适当的调整和扩展。


# 初始化使用

自行配置完毕后请执行：
```
flask db init #用于生成数据库迁移文件
```

# 数据库迁移

Flask-Migrate是一个用于在Flask应用中进行数据库迁移的扩展。它基于Alembic，并提供了一种简便的方式来管理数据库模式的变更。

下面是本模板使用Flask-Migrate的一般步骤：

1. 创建迁移存储库（migration repository）：
   在终端中导航到你的应用目录，并运行以下命令：
   ```
   flask db init
   ```

   这将在你的应用目录中创建一个`migrations`文件夹，用于存储数据库迁移相关的文件。

2. 创建初始数据库迁移脚本：
   运行以下命令来生成初始的数据库迁移脚本：
   ```
   flask db migrate -m "initial migration"
   ```

   这将根据你的模型定义生成一个初始的数据库迁移脚本，该脚本将包含创建表格的操作。

3. 应用数据库迁移：
   运行以下命令来应用数据库迁移：
   ```
   flask db upgrade
   ```

   这将在你的数据库中执行迁移脚本，创建相应的表格。

4. 模型更改后的数据库迁移：
   每当你对模型进行更改时，需要生成一个新的数据库迁移脚本，并将其应用到数据库中。

   生成迁移脚本：
   ```
   flask db migrate -m "description of migration"
   ```

   应用迁移脚本：
   ```
   flask db upgrade
   ```

   这样，你的数据库将根据模型的更改进行更新。

这些是使用Flask-Migrate进行数据库迁移的基本步骤。你可以根据自己的需求和模型更改的复杂程度进行调整。还有其他的命令和选项可供使用，你可以查阅Flask-Migrate的官方文档以获取更多详细信息：https://flask-migrate.readthedocs.io/

# 生成依赖文件

要生成`requirements.txt`文件，可以使用`pip`工具来帮助你导出当前Python环境中已安装的所有包及其版本信息。

请按照以下步骤进行操作：

1. 打开终端或命令提示符，进入你的项目目录。

2. （可选）创建并激活一个虚拟环境（如果你在项目中使用虚拟环境）。

3. 运行以下命令来生成`requirements.txt`文件：
   ```
   pip freeze > requirements.txt
   ```

   这将列出当前环境中安装的所有Python包及其版本，并将其写入到`requirements.txt`文件中。

4. 生成的`requirements.txt`文件将保存在你的项目目录下。

你可以使用文本编辑器或其他工具打开`requirements.txt`文件，查看其中列出的包和版本信息。

注意事项：
- 如果你只想包含项目的依赖项而不包括所有已安装的包，你可以在生成`requirements.txt`之前先激活你的虚拟环境，以确保只包含项目所需的包。
- 当你使用虚拟环境时，确保在激活虚拟环境后执行`pip freeze`命令，以便只导出虚拟环境中的包。

这样，你就可以生成一个`requirements.txt`文件，其中包含了你项目所需的所有依赖包及其版本信息。这对于共享和重现项目的环境非常有用。

5. 安装依赖，打开终端或命令提示符，导航到项目的根目录，然后运行以下命令安装依赖：

```
pip install -r requirements.txt
```

# 关系型数据库

在 Flask 中，可以使用关系型数据库（如 SQLAlchemy）来定义和管理表之间的关系。下面是一个简单的示例，展示了用户（User）和帖子（Post）之间的一对多关系。

在 `models.py` 文件中定义用户和帖子的模型类，并添加外键关系：

```python
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}')"
```

在这个示例中，`User` 类表示用户模型，`Post` 类表示帖子模型。在 `User` 类中，我们定义了一个名为 `posts` 的关系属性，通过 `db.relationship` 声明了一对多的关系。`backref='author'` 参数允许通过帖子对象访问其作者（即用户）对象。

在 `Post` 类中，我们定义了一个名为 `user_id` 的外键字段，并通过 `db.ForeignKey` 声明了与用户表的关联关系。

这样，我们就建立了一个简单的一对多关系，一个用户可以有多个帖子，而每个帖子都属于一个用户。

请注意，以上示例是一种简化的方式来表示关系，仅用于说明基本概念。在实际项目中，您可能需要更多的字段和复杂的关系定义，具体取决于您的应用程序需求。

通过在 `Post` 模型中定义了 `user_id` 字段和关联关系后，您可以使用 `author` 属性来访问每篇帖子的作者（即用户）对象。以下是示例代码：

```python
# 获取一篇帖子
post = Post.query.first()

# 通过帖子对象访问其作者
author = post.author
```

在上述示例中，`post` 是一个 `Post` 对象，通过调用 `post.author` 属性，可以获取到该帖子的作者对象。

您可以根据您的项目需求，在视图函数中使用类似的方式来访问帖子的作者，然后在模板中使用这些信息进行显示或其他操作。

# workflow

用于打包三个平台的二进制文件，使用方法为：

替换.github\workflows\auto_release.yml文件中所有${PROJECT_NAME}为你的项目的名字