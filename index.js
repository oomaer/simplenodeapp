const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const cors = require('cors');
const mongoose = require('mongoose');
const ejs = require('ejs');

const {addUser, loginUser} = require('./controller/userController');


//load view engine
app.set('view engine', 'ejs');
app.use(cors());
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());



const database_name = 'simplenodeapp'

const MongoURL = `mongodb+srv://newuser:newuser@cluster2.p9pvqzf.mongodb.net/${database_name}?retryWrites=true&w=majority`


mongoose.connect(MongoURL, {    
        useUnifiedTopology: true,
        useNewUrlParser: true,
        autoIndex: true, //make this also true})
    })
    .then(result => {
        let port = (process.env.PORT || 5051);
        app.listen(port);
        console.log('server running on port: ' + port);
    })
    .catch((err => console.log(err)));
   


app.get('/', (req, res) => {
    res.render("index");
})

app.get('/register', (req, res) => {
    res.render("register");
})

app.get('/login', (req, res) => {
    res.render("login");
})

app.post('/register', addUser);
app.post('/login', loginUser);