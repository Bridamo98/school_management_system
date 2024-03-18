
import Renderer from '../../renderer/Renderer';
import Factory from '../../factory/Factory';
import Templates from '../../templates/Templates';
import RegisterStudentFormModel from '../../models/RegisterStudentFormModel';

class RegisterStudentFormController {

  static initController (): void {
    const registerStudentForm = Factory.createRegisterStudentForm()
    Renderer.renderRegisterStudentForm(registerStudentForm, Templates.getRegisterStudentTemplate());
    const formElement = document.querySelector('form');
    formElement?.addEventListener('submit', (event) => {
      event.preventDefault();
      this.handleFormSubmit(registerStudentForm);
    });
  }

  static handleFormSubmit(form: RegisterStudentFormModel) {
    const nameInput = document.getElementById(form.nameField.id) as HTMLInputElement;
    const gradeInput = document.getElementById(form.gradeField.id) as HTMLInputElement;
    const ageInput = document.getElementById(form.ageField.id) as HTMLInputElement;
    if (!nameInput.value || !gradeInput.value || !ageInput.value) {
      alert('All fields are required');
      return;
    }

    form.setNameValue(nameInput.value);
    form.setCourseValue(gradeInput.value);
    form.setAgeValue(ageInput.value);

    alert('Valid form');
  }
}


export default RegisterStudentFormController
