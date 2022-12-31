const User = require('../models/User');

const addUser = async (req, res) => {
    const data = req.body;
    try{
        const user = new User({
            name: data.name,
            email: data.email,
            password: data.password
        })

        const result = await user.save()
        res.status(200).json({message: "Registration Successful"})

    }catch(err){
        if(err.code === 11000){
            res.status(409).json({message: "User already exists. Go to Login Page to Log into the account"})
        }
        else{
            res.status(401).json({message: err.message})
        }
        
        console.log(err);
    }
}


const loginUser = async (req, res) => {
    const data = req.body;
    try{
        const user = await User.findOne({email: data.email})
        if(user.password === data.password){
            res.status(200).json({message: "Login successful"})
        }else{
            res.status(401).json({message: "Invalid credentials"})
        }
    }catch(err){
        res.status(401).json({message: "Invalid credentials"})
        console.log(err);
    }
}

module.exports = {addUser, loginUser}