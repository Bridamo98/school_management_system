
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
    const courseInput = document.getElementById(form.courseField.id) as HTMLInputElement;
    const ageInput = document.getElementById(form.ageField.id) as HTMLInputElement;
    if (!nameInput.value || !courseInput.value || !ageInput.value) {
      alert('Todos los campos son obligatorios. Por favor, complete todos los campos.');
      return;
    }

    form.setNameValue(nameInput.value);
    form.setCourseValue(courseInput.value);
    form.setAgeValue(ageInput.value);

    alert('Formulario valido');
  }
}


export default RegisterStudentFormController
