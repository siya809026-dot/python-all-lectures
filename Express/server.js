const express = require('express')

const app = express()

const PORT = 3000

app.get("/RAM",(req,res)=>{
    res.send("Sita Ram")
})

app.get("/siya",(req,res)=>{
    res.send("jay shri Ram")
})

app.listen(PORT , ()=>{
    console.log("Server is on port 3000 jai shri ram")
})