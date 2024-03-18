class Templates {
  static getRegisterStudentTemplate (): string {
    return `
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register Student</title>
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
