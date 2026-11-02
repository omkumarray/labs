const express = require('express');
const app = express();

app.use(express.json());
app.use(express.static('public'));

let items = [
    { id: 1, name: 'NodeJs' },
    { id: 2, name: 'ExpressJs' },
    { id: 3, name: 'ReactJs' },
    { id: 4, name: 'MongoDB' }
];
app.get('/items', (req, res) => {
    res.json(items);
});
app.post('/items', (req, res) => {
    const item = {
        id: Date.now(),
        name: req.body.name
    };
    items.push(item);
    res.json(items);
});
app.delete('/items/:id', (req, res) => {
    items = items.filter(item => item.id != req.params.id);
    res.json(items);
});
app.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});
