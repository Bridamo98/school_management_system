class Templates {
  static getRegisterStudentTemplate (): string {
    return `
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register Student</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh; /* Make the body take the full height of the viewport */
            margin: 0; /* Remove default margin */
            background-color: #f4f4f4; /* Light gray background */
        }

        h1 {
            color: #333; /* Dark gray text color */
        }

        form {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }

        label {
            margin: 10px 0;
            color: #333; /* Dark gray text color */
        }

        input {
            padding: 8px;
            margin: 5px 0 15px;
            width: 200px;
            border: 1px solid #3498db; /* Blue border */
            border-radius: 5px;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            background-color: #3498db; /* Blue button background color */
            color: #fff; /* White text color */
            border: none;
            border-radius: 5px;
        }

        button:hover {
            background-color: #2980b9; /* Darker blue on hover */
        }
    </style>
    </head>
    <body>
      <h1>Register Student</h1>
      <form>
          <label for="{{name.name}}">{{name.label}}:</label>
          <input type="{{name.type}}" id="{{name.id}}" value="{{name.value}}" />
          <label for="{{grade.name}}">{{grade.label}}:</label>
          <input type="{{grade.type}}" id="{{grade.id}}" value="{{grade.value}}" />
          <label for="{{age.name}}">{{age.label}}:</label>
          <input type="{{age.type}}" id="{{age.id}}" value="{{age.value}}" />
          <button type="submit">Register</button>
      </form>
    </body>
    </html>
    `
  }
}

export default Templates
