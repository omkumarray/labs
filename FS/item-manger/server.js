const express = require('express');
const path = require('path');
const app = express();

app.use(express.json());
app.use(express.static('public'));

let items = [
    { id: 1, name: 'NodeJs' },
    { id: 2, name: 'ExpressJs' },
    { id: 3, name: 'ReactJs' },
    { id: 4, name: 'MongoDB' }
];

app.get('/api/items', (req, res) => res.json(items));

app.post('/api/items', (req, res) => {
    const item = { id: Date.now(), name: req.body.name };
    items.push(item);
    res.json(item);
});

app.delete('/api/items/:id', (req, res) => {
    items = items.filter(i => i.id != req.params.id);
    res.json({ message: 'Deleted' });
});

app.listen(8000, () => {
    console.log('Server running at http://localhost:8000');
});