const express = require('express');
const session = require('express-session');
const app = express();

app.use(express.urlencoded({ extended: true }));

app.use(session({
    secret: 'mySecretKey',
    resave: false,
    saveUninitialized: false
}));

app.get('/login', (req, res) => {
    res.send(`
        <h2>Login</h2>
        <form method="POST" action="/login">
            <input name="username" placeholder="Username" required><br><br>
            <input name="password" type="password" placeholder="Password" required><br><br>
            <button type="submit">Login</button>
        </form>
    `);
});

app.post('/login', (req, res) => {
    const { username, password } = req.body;

    if (username === 'Akshay' && password === '1234') {
        req.session.user = username;
        res.redirect('/dashboard');
    } else {
        res.send('Invalid username or password. <a href="/login">Try again</a>');
    }
});

app.get('/dashboard', (req, res) => {
    if (req.session.user) {
        res.send(`
            <h1>Welcome, ${req.session.user}!</h1>
            <p>You are logged in.</p>
            <a href="/logout">Logout</a>
        `);
    } else {
        res.redirect('/login');
    }
});

app.get('/logout', (req, res) => {
    req.session.destroy(() => {
        res.redirect('/login');
    });
});

app.get('/', (req, res) => {
    res.redirect('/login');
});

app.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});