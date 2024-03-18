interface FormField {
  name: string
  type: string
  label: string
  value: string
  id: string
}

class RegisterStudentFormModel {
  nameField: FormField
  gradeField: FormField
  ageField: FormField

  constructor (name: FormField, grade: FormField, age: FormField) {
    this.nameField = name
    this.gradeField = grade
    this.ageField = age
  }

  setNameValue(value: string) {
    this.nameField = { ...this.nameField, value: value };
  }

  setCourseValue(value: string) {
    this.gradeField = { ...this.gradeField, value: value };
  }

  setAgeValue(value: string) {
    this.ageField = { ...this.ageField, value: value };
  }
}

export default RegisterStudentFormModel
