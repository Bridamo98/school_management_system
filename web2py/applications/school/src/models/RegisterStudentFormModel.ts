interface FormField {
  name: string
  type: string
  label: string
  value: string
  id: string
}

class RegisterStudentFormModel {
  nameField: FormField
  courseField: FormField
  ageField: FormField

  constructor (name: FormField, course: FormField, age: FormField) {
    this.nameField = name
    this.courseField = course
    this.ageField = age
  }

  setNameValue(value: string) {
    this.nameField = { ...this.nameField, value: value };
  }

  setCourseValue(value: string) {
    this.courseField = { ...this.courseField, value: value };
  }

  setAgeValue(value: string) {
    this.ageField = { ...this.ageField, value: value };
  }
}

export default RegisterStudentFormModel
