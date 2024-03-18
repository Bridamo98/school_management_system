import RegisterStudentFormModel from '../models/RegisterStudentFormModel'

class Factory {
  static createRegisterStudentForm (): RegisterStudentFormModel {
    return new RegisterStudentFormModel(
      { name: 'name', type: 'text', label: 'Name', value: "", id: "name"},
      { name: 'grade', type: 'text', label: 'Grade', value: "", id: "grade"},
      { name: 'age', type: 'text', label: 'Age', value: "", id: "age"})
  }
}

export default Factory
