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
        .replace('{{grade.name}}', registerStudentForm.gradeField.name)
        .replace('{{grade.type}}', registerStudentForm.gradeField.type)
        .replace('{{grade.label}}', registerStudentForm.gradeField.label)
        .replace('{{grade.value}}', registerStudentForm.gradeField.value)
        .replace('{{grade.id}}', registerStudentForm.gradeField.id)
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
