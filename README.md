# CMT120 Coursework 2 - Dynamic Website-coursework2
<h1>Digital Portfolio - Flaskapp</h1>


<h2>URL of the website on Openshift server</h2>
http://c-21114732-cmt-120-cw-2-git-c21114732-cmt120-cw22.apps.openshift.cs.cf.ac.uk

<h2>Overview</h2>
Digital Portfolio with Flask framework

<h3>Key features:</h3>
<ul>
<li>User authentication required to post comment on blog articles</li>
<li>Flask-Mail appication to set up SMTP server to send messages(emails) through flask application</li>
<li>Websites rich in links to other resourceful pages like GitHub, GitHub pages, LinkedIn, and mail</li>
</ul>

## Local Development (Empty Site)

> Creates a fresh local instance with an empty database.

### 1) Create & activate a virtual environment

**Windows (PowerShell)**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
````

**Windows (cmd.exe)**

```bat
python -m venv venv
.\venv\Scripts\activate.bat
```

**macOS / Linux (POSIX)**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Initialize the database

```bash
python db_creation.py
```

Follow the prompts:

* Press **Enter** to confirm creation.
* Set an **Admin password** (used to create the initial Admin account).

### 4) Run the app

**Option A — via Flask**

```bash
# Windows (PowerShell)
set FLASK_APP=wsgi.py
flask run

# macOS / Linux
export FLASK_APP=wsgi.py
flask run
```

**Option B — directly**

```bash
python wsgi.py
```

---

## Remote Deployment

### Prerequisites (environment variables)

Inject these into your runtime (container/orchestrator):

* `ENV_TYPE` — `PROD` or `STAGING`
* `MYSQL_ADDRESS` — MySQL host (e.g., `db:3306` or `127.0.0.1:3306`)
* `MYSQL_DB_NAME` — database name
* `MYSQL_USER` — database user
* `MYSQL_PASSWORD` — database user password

> The app expects **MySQL**. Other engines can work by changing the SQLAlchemy **dialect + driver** in `cfg.py` (e.g., `postgresql+psycopg2://…`). Ensure the environment variables are set and the final Database URI is correct (check logs if unsure).

### Initial setup (first deploy)

On the deployment container shell:

```bash
python db_creation.py
```

Verify the printed **address** and **name** match your target DB, press **Enter** to confirm, then choose the **Admin password** when prompted.

### Start the service

Restart/redeploy your service or pod to begin serving the application.



<h2>References</h2>
<blockquote>Pallets. (2007)<i> ‘Werkzeug Utilities’. </i>Available at: https://werkzeug.palletsprojects.com/en/2.2.x/utils/#module-werkzeug.security [Accessed on: 19 January 2023]</blockquote>

<blockquote>freeCodeCamp.org(2019). <i>‘Web Programming with Flask-Intro to Computer Science - Harvard's CS50 (2018).</i> Available at: https://www.youtube.com/watch?v=zdgYw-3tzfI&list=PLWKjhJtqVAbmGw5fN5BQlwuug-8bDmabi&index=13 [Accessed: 13 January 2023]</blockquote>

<blockquote><i>flask mail documentation. </i>Available at: https://pythonhosted.org/Flask-Mail/ [Accessed: 14 January 2023]</blockquote>

<blockquote>TechwithTim(2021).<i>‘Flask User Authentication and Security’.</i> Available at: https://www.youtube.com/watch?v=W4GItcW7W-U&list=PLzMcBGfZo4-nK0Pyubp7yIG0RdXp6zklu&index=3 [Accessed: 13 January 2023]</blockquote>

<blockquote> EasyTutorials(2022). <i>How To Make A Portfolio Website Using HTML CSS JS.</i> Available at: https://www.youtube.com/watch?v=0YFrGy_mzjY [Accessed: 10 January 2023] </blockquote>

<blockquote>TechwithTim(2021).<i>‘Creating and deleting posts’.</i> Available at: https://www.youtube.com/watch?v=f_bml-MILAs&list=PLzMcBGfZo4-nK0Pyubp7yIG0RdXp6zklu&index=4 [Accessed: 15 January 2023]</blockquote>

<blockquote> T. Ahmed(2021).<i> Build a portfolio website using HTML & CSS.</i> Available at: https://www.youtube.com/watch?v=lgeoAUvoRJU [Accessed: 10 January 2023]</blockquote>

<blockquote> L. ALLEDJI(2022).<i> How to send an e-mail with Flask and Flask-Mail?</i> Available at: https://medium.com/@lewis.devs/how-to-send-an-e-mail-with-flask-a13e751a5cab  [Accessed: 13 January 2023]</blockquote>
