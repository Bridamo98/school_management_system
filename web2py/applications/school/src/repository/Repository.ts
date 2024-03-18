import RegisterStudentFormModel from "../models/RegisterStudentFormModel";
import isNumeric from "../utils/Utils"
import axios from "axios";

class Repository {
  static async registerStudent(
    form: RegisterStudentFormModel,
    formElement: HTMLFormElement
  ): Promise<any> {
    const apiUrl = "/school/api/register_student";

    const requestData = {
      name: form.nameField.value,
      grade: form.gradeField.value,
      age: form.ageField.value,
    };


    if (!isNumeric(form.ageField.value)) {
      alert("Age must be an integer");
      return;
    }

    return axios
      .post(apiUrl, requestData)
      .then((response) => {
        alert("Student registered");
        // console.log('Registration successful:', response.data);
        formElement.reset();
        return response.data;
      })
      .catch((error) => {
        alert("Student registration was not possible");
        // console.error('Registration failed:', error);
        throw error;
      });
  }
}

export default Repository;
