import type RegisterStudentFormModel from '../models/RegisterStudentFormModel'

class Renderer {
  static renderRegisterStudentForm (registerStudentForm: RegisterStudentFormModel, template: string): void {
    const htmlTemplate = template
    const html = `
      ${htmlTemplate
        .replace('{{name.name}}', registerStudentForm.nameField.name)
        .replace('{{name.type}}', registerStudentForm.nameField.type)
        .replace('{{name.label}}', registerStudentForm.nameField.label)
        .replace('{{name.value}}', registerStudentForm.nameField.value)
        .replace('{{name.id}}', registerStudentForm.nameField.id)
        .replace('{{course.name}}', registerStudentForm.courseField.name)
        .replace('{{course.type}}', registerStudentForm.courseField.type)
        .replace('{{course.label}}', registerStudentForm.courseField.label)
        .replace('{{course.value}}', registerStudentForm.courseField.value)
        .replace('{{course.id}}', registerStudentForm.courseField.id)
        .replace('{{age.name}}', registerStudentForm.ageField.name)
        .replace('{{age.type}}', registerStudentForm.ageField.type)
        .replace('{{age.label}}', registerStudentForm.ageField.label)
        .replace('{{age.value}}', registerStudentForm.ageField.value)
        .replace('{{age.id}}', registerStudentForm.ageField.id)
      }
      `
      document.body.innerHTML = html;
  }
}

export default Renderer
