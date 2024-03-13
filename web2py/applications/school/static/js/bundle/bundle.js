(()=>{"use strict";var e={115:(e,t,a)=>{Object.defineProperty(t,"__esModule",{value:!0});const n=a(292);t.default=class{static createRegisterStudentForm(){return new n.default({name:"name",type:"text",label:"Name",value:"",id:"name"},{name:"course",type:"text",label:"Course",value:"",id:"course"},{name:"age",type:"text",label:"Age",value:"",id:"age"})}}},292:(e,t)=>{Object.defineProperty(t,"__esModule",{value:!0}),t.default=class{constructor(e,t,a){this.nameField=e,this.courseField=t,this.ageField=a}setNameValue(e){this.nameField=Object.assign(Object.assign({},this.nameField),{value:e})}setCourseValue(e){this.courseField=Object.assign(Object.assign({},this.courseField),{value:e})}setAgeValue(e){this.ageField=Object.assign(Object.assign({},this.ageField),{value:e})}}},193:(e,t,a)=>{Object.defineProperty(t,"__esModule",{value:!0});const n=a(467);t.default=class{static initProcess(){n.default.initController()}}},95:(e,t)=>{Object.defineProperty(t,"__esModule",{value:!0}),t.default=class{static renderRegisterStudentForm(e,t){const a=`\n      ${t.replace("{{name.name}}",e.nameField.name).replace("{{name.type}}",e.nameField.type).replace("{{name.label}}",e.nameField.label).replace("{{name.value}}",e.nameField.value).replace("{{name.id}}",e.nameField.id).replace("{{course.name}}",e.courseField.name).replace("{{course.type}}",e.courseField.type).replace("{{course.label}}",e.courseField.label).replace("{{course.value}}",e.courseField.value).replace("{{course.id}}",e.courseField.id).replace("{{age.name}}",e.ageField.name).replace("{{age.type}}",e.ageField.type).replace("{{age.label}}",e.ageField.label).replace("{{age.value}}",e.ageField.value).replace("{{age.id}}",e.ageField.id)}\n      `;document.body.innerHTML=a}}},467:(e,t,a)=>{Object.defineProperty(t,"__esModule",{value:!0});const n=a(95),l=a(115),r=a(83);t.default=class{static initController(){const e=l.default.createRegisterStudentForm();n.default.renderRegisterStudentForm(e,r.default.getRegisterStudentTemplate());const t=document.querySelector("form");null==t||t.addEventListener("submit",(t=>{t.preventDefault(),this.handleFormSubmit(e)}))}static handleFormSubmit(e){const t=document.getElementById(e.nameField.id),a=document.getElementById(e.courseField.id),n=document.getElementById(e.ageField.id);t.value&&a.value&&n.value?(e.setNameValue(t.value),e.setCourseValue(a.value),e.setAgeValue(n.value),alert("Formulario valido")):alert("Todos los campos son obligatorios. Por favor, complete todos los campos.")}}},83:(e,t)=>{Object.defineProperty(t,"__esModule",{value:!0}),t.default=class{static getRegisterStudentTemplate(){return'\n    <html lang="en">\n    <head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Register Student</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            display: flex;\n            flex-direction: column;\n            align-items: center;\n            justify-content: center;\n            height: 100vh; /* Make the body take the full height of the viewport */\n            margin: 0; /* Remove default margin */\n            background-color: #f4f4f4; /* Light gray background */\n        }\n\n        h1 {\n            color: #333; /* Dark gray text color */\n        }\n\n        form {\n            display: flex;\n            flex-direction: column;\n            align-items: center;\n            margin-top: 20px;\n        }\n\n        label {\n            margin: 10px 0;\n            color: #333; /* Dark gray text color */\n        }\n\n        input {\n            padding: 8px;\n            margin: 5px 0 15px;\n            width: 200px;\n            border: 1px solid #3498db; /* Blue border */\n            border-radius: 5px;\n        }\n\n        button {\n            padding: 10px 20px;\n            font-size: 16px;\n            cursor: pointer;\n            background-color: #3498db; /* Blue button background color */\n            color: #fff; /* White text color */\n            border: none;\n            border-radius: 5px;\n        }\n\n        button:hover {\n            background-color: #2980b9; /* Darker blue on hover */\n        }\n    </style>\n    </head>\n    <body>\n      <h1>Register Student</h1>\n      <form>\n          <label for="{{name.name}}">{{name.label}}:</label>\n          <input type="{{name.type}}" id="{{name.id}}" value="{{name.value}}" />\n          <label for="{{course.name}}">{{course.label}}:</label>\n          <input type="{{course.type}}" id="{{course.id}}" value="{{course.value}}" />\n          <label for="{{age.name}}">{{age.label}}:</label>\n          <input type="{{age.type}}" id="{{age.id}}" value="{{age.value}}" />\n          <button type="submit">Register</button>\n      </form>\n    </body>\n    </html>\n    '}}}},t={};(function a(n){var l=t[n];if(void 0!==l)return l.exports;var r=t[n]={exports:{}};return e[n](r,r.exports,a),r.exports})(193).default.initProcess()})();