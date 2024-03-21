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
        alert('STUDENT REGISTERED!.\n\n' + response.data.message);
        formElement.reset();
        return response.data;
      })
      .catch((error) => {
        alert(error.data);
        // console.error('Registration failed:', error);
        throw error;
      });
  }
}

export default Repository;
