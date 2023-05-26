//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require('mongoose');
const date = require(__dirname + "/date.js");
const _ = require("lodash");

const app = express();

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));


mongoose.connect('mongodb+srv://mohanadEldalie:mohanad124578@cluster0.ibvhuvi.mongodb.net/todoListDB');

const taskSchema = new mongoose.Schema({
  name: String,
});

const Task = mongoose.model("Task", taskSchema);

const listSchema = new mongoose.Schema({
  name: String,
  tasks: [taskSchema]
});

const List = mongoose.model("List", listSchema);


app.get("/", function(req, res) {
  const day = date.getDate();
  var allLists = []

  List.find().then(function(lists) {
    allLists = lists; 
  }).catch(function(err) {
    console.log(err);
  });;

  Task.find().then(function(tasks) {
    res.render("list", {listTitle: day, allTasks: tasks, allLists: allLists});
  }).catch(function(err) {
    console.log(err);
  });;
});

app.post("/", function(req, res){
  const list = req.body.list;
  const task = req.body.newItem;

  var newTask = new Task({
    name: task
  })

  if(list === date.getDate()){
    newTask.save();
    res.redirect("/");
  } else{
    List.findOne({name: list}).then(function(list){
      list.tasks.push(newTask);
      list.save();
      res.redirect("/" + list.name)
    })
  }

});

app.post("/delete", function(req, res){
  const checkedTaskId = req.body.checkbox;
  const listName = req.body.listName;

  if(listName == date.getDate()){
    Task.deleteOne({_id: checkedTaskId}).catch(function(err){
      console.log(err);
    });
  
    res.redirect("/")
  } else{
    List.findOneAndUpdate({name: listName}, {$pull: {tasks: {_id: checkedTaskId}}}).then(function(results) {
      res.redirect("/" + listName);
    }).catch(function(err) {
      console.log();
    });;
  }
})

app.get("/:listName", function(req,res){
  var costumeListName = _.capitalize(req.params.listName);
  
  var allLists = []
  
  List.find().then(function(lists) {
    allLists = lists; 
  }).catch(function(err) {
    console.log(err);
  });;

  List.findOne({name: costumeListName}).then(function(list){
    if(!list){
      const list = new List({
        name: costumeListName,
        tasks: []
      })
    
      list.save();
      res.redirect("/" + costumeListName, {allLists: allLists})
    } else{
      res.render("list", {listTitle: list.name, allTasks: list.tasks, allLists: allLists})
    }
  }).catch(function(err){
    console.log(err);
  });
});

app.post("/:listName", function(req, res){
  var costumeListName = req.params.listName;

  res.redirect("/" + costumeListName, {allLists: allLists})
})

app.get("/about", function(req, res){
  res.render("about");
});


app.listen(3000, function() {
  console.log("Server started on port 3000");
});
