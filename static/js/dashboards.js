// // start logout coding
// var welcome_el = document.querySelector("#welcome");
// var username = sessionStorage.getItem("username");

// if(username == null){
//     document.body.innerHTML = "<h1>Illigal action perform</h1>";
//     document.body.classList.add("illigal");
// }

// var logout_btn = document.querySelector("#logout-btn");
// logout_btn.onclick = function(){
//     window.location = "../index.html";
//     sessionStorage.removeItem("username");
// }

// var user_data = JSON.parse(localStorage.getItem(username));
// welcome_el.innerHTML = "Hello"+user_data.f_name+ " " + user_data.l_name;


// // start contact list coding

// var create_btn = document.querySelector(".create-btn");
// var update_btn = document.querySelector(".update-btn");
// var contact_detail = document.querySelector(".contact-details");
// var input_name = document.querySelector(".name");
// var input_number = document.querySelector(".number");

// create_btn.onclick = function(e){
//     e.preventDefault();
//     if(input_name.value != "" && input_number.value != ""){
//         newConatctApp();
//         updateLocalStorage();
//     }
//     else{
//         alert("Input field is empty !");
//     }
// }

// if(localStorage.getItem(username+"_list") != null){
//     var array_list = JSON.parse(localStorage.getItem(username+"_list"));
//     array_list.forEach(task =>{
//         newConatctApp(task)
//     })
// }

// function newConatctApp(task){
//     var i;
//     var name = input_name.value;
//     var number  = input_number.value;
    
//     if(task){
//         name = task.co_name;
//         number = task.co_number;
//     }

//     var accordion = document.createElement("DIV");
//     accordion.classList = "accordion mb-3";

//     var all_accordions = contact_detail.getElementsByClassName("accordion");
//     for(i=0; i<all_accordions.length; i++){

//     }

//     var accordion_item = document.createElement("DIV");
//     accordion_item.classList = "accordion-item";
//     accordion.append(accordion_item);
//     var accordion_header = document.createElement("H5");
//     accordion_header.classList = "accordion-header";
//     accordion_item.append(accordion_header);
//     var button = document.createElement("BUTTON");
//     button.classList = "accordion-button";
//     button.innerText = name;
//     button.setAttribute("data-bs-toggle","collapse");
//     button.setAttribute("data-bs-target","#collapse-"+i);
//     accordion_header.append(button);
//     var accordion_collpase = document.createElement("DIV");
//     accordion_collpase.classList = "accordion-collapse collapse";
//     accordion_collpase.id = "collapse-"+i;
//     accordion_item.append(accordion_collpase);
//     var accordion_body = document.createElement("DIV");
//     accordion_body.classList = "accordion-body";
//     accordion_collpase.append(accordion_body);
//     var row = document.createElement("DIV");
//     row.classList = "row";
//     accordion_body.append(row);
//     var col_one = document.createElement("DIV");
//     col_one.classList = "col-md-6";
//     row.append(col_one);
//     var h5 = document.createElement("H5");
//     h5.innerText = name;
//     h5.id = "contact-"+i;
//     col_one.append(h5);
//     var p = document.createElement("P");
//     p.innerText = number;
//     col_one.append(p);
//     var col_two = document.createElement("DIV");
//     col_two.classList = "col-md-6 d-flex justify-content-around align-items-center position-relative";
//     col_two.innerHTML = '<i class="fa-regular fa-message"></i><i class="fa-solid fa-square-phone"></i><i class="fa-solid fa-ellipsis-vertical op-btn"></i>';
//     row.append(col_two);
//     var option_box = document.createElement("DIV");
//     option_box.classList = "option-box";
//     option_box.innerHTML = '<i class="fa-regular fa-pen-to-square"></i><i class="fa-solid fa-trash"></i>';
//     col_two.append(option_box);
//     contact_detail.append(accordion);

//     input_name.value = "";
//     input_number.value = "";


//     var i_tag = option_box.getElementsByTagName("I");
    
//     // start update coding

//     i_tag[0].onclick = function(){
//         var parent = this.parentElement.parentElement.parentElement;
//         var h5 = parent.getElementsByTagName("H5");
//         var p = parent.getElementsByTagName("P");

//         var edited_name = h5[0].innerHTML;
//         var edited_con = p[0].innerHTML;
        
//         input_name.value = edited_name;
//         input_number.value = edited_con;
//         input_name.focus();
//         create_btn.classList.add("d-none");
//         update_btn.classList.remove("d-none");

//         update_btn.onclick = function(){
//             var id = h5[0].getAttribute("id").replace("contact-","");
//             var co_name = input_name.value;
//             var co_number = input_number.value;
//             updateLocalStorage(co_name,co_number,id);
//         }

//     }

//     // start delete coding
//     i_tag[1].onclick = function(){
//         var cnf = window.confirm("Do you wanna delete ?");
//         if(cnf){
//             accordion.remove();
//             updateLocalStorage();
//         }
//         else{
//             alert("Your data is safe !");
//         }
//     }

//     // start option box coding

//     var op_btn = document.querySelectorAll(".op-btn");
//     for(i=0;i<op_btn.length;i++){
//         op_btn[i].onclick = function(){
//             var parent = this.parentElement;
//             var op_box = parent.querySelector(".option-box");
//             op_box.classList.toggle("active");
//         }
//     }

// }

// // start update localstorage coding
// function updateLocalStorage(name,number,id){
    
//     if(name != "" && number != ""){
//         array_list[id] = {
//             co_name : name,
//             co_number : number
//         }
//     }
//     else{
//         var i;
//         array_list = [];
//         var accordion_el = contact_detail.querySelectorAll(".accordion");
//         for(i=0;i<accordion_el.length;i++){
//             var h5 = accordion_el[i].getElementsByTagName("H5");
//             var p = accordion_el[i].getElementsByTagName("P");
//             array_list.push({
//                 co_name : h5[1].innerHTML,
//                 co_number : p[0].innerHTML
//             });
//         }
//     }

    
//     localStorage.setItem(username+"_list",JSON.stringify(array_list));
// }

// // start search coding

// function mySearch(){
//     var i,btn,textValue;
//     var input = document.querySelector("#search").value;
//     var filter = input.toUpperCase();
//     var accordion = contact_detail.querySelectorAll(".accordion");
//     for(i=0;i<accordion.length;i++){
//         btn = accordion[i].getElementsByTagName("BUTTON")[0];
//         textValue = btn.innerText;
//         if(textValue.toUpperCase().indexOf(filter) > -1){
//             accordion[i].style.display = "";
//         }
//         else{
//             accordion[i].style.display = "none";
//         }
//     }
// }