# Flask-website-coursework2
<h1>Digital Portfolio - Flaskapp</h1>


<h2>URL of my website on Openshift server</h2>
http://c-21114732-cmt-120-cw-2-git-c21114732-cmt120-cw22.apps.openshift.cs.cf.ac.uk

<h2>Overview</h2>
Digital Portfolio with Flask framework

<h3>Key features:</h3>
<ul>
<li>User authentication required to post comment on blog articles</li>
<li>Flask-Mail appication to set up SMTP server to send messages(emails) through flask application</li>
<li>Websites rich in links to other resourceful pages like GitHub, GitHub pages, LinkedIn, and mail</li>
</ul>

<h3>Comment features</h3>
Example email that is already on the database:

email: cakes@gmail.com <br>
password: 1234567


<h2>Key Functionality</h2>
<ul>
<li>werkzeug.security
Used to hash passwords, which encodes the existing password to store them securely. </li>

<li>DB connection processing in SQLAlchemy</li>

<li>Flask-Login - user session management
Easily remember logins, logouts and sessions</li>

<li>Flask-Mail
Sets up SMTP connection to send messages through flask application</li>

<li>Pagination functionality using Flask-SQLAlchemy</li>

<li>Downloading files using the Download attribute – CV file</li>
</ul>

<h2>References</h2>
<blockquote>Pallets. (2007)<i> ‘Werkzeug Utilities’. </i>Available at: https://werkzeug.palletsprojects.com/en/2.2.x/utils/#module-werkzeug.security [Accessed on: 19 January 2023]</blockquote>

<blockquote>freeCodeCamp.org(2019). <i>‘Web Programming with Flask-Intro to Computer Science - Harvard's CS50 (2018).</i> Available at: https://www.youtube.com/watch?v=zdgYw-3tzfI&list=PLWKjhJtqVAbmGw5fN5BQlwuug-8bDmabi&index=13 [Accessed: 13 January 2023]</blockquote>

<blockquote><i>flask mail documentation. </i>Available at: https://pythonhosted.org/Flask-Mail/ [Accessed: 14 January 2023]</blockquote>

<blockquote>TechwithTim(2021).<i>‘Flask User Authentication and Security’.</i> Available at: https://www.youtube.com/watch?v=W4GItcW7W-U&list=PLzMcBGfZo4-nK0Pyubp7yIG0RdXp6zklu&index=3 [Accessed: 13 January 2023]</blockquote>

<blockquote> EasyTutorials(2022). <i>How To Make A Portfolio Website Using HTML CSS JS.</i> Available at: https://www.youtube.com/watch?v=0YFrGy_mzjY [Accessed: 10 January 2023] </blockquote>

<blockquote>TechwithTim(2021).<i>‘Creating and deleting posts’.</i> Available at: https://www.youtube.com/watch?v=f_bml-MILAs&list=PLzMcBGfZo4-nK0Pyubp7yIG0RdXp6zklu&index=4 [Accessed: 15 January 2023]</blockquote>

<blockquote> T. Ahmed(2021).<i> Build a portfolio website using HTML & CSS.</i> Available at: https://www.youtube.com/watch?v=lgeoAUvoRJU [Accessed: 10 January 2023]</blockquote>

<blockquote> L. ALLEDJI(2022).<i> How to send an e-mail with Flask and Flask-Mail?</i> Available at: https://medium.com/@lewis.devs/how-to-send-an-e-mail-with-flask-a13e751a5cab  [Accessed: 13 January 2023]</blockquote>
