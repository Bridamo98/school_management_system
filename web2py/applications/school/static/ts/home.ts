function registerStudent (): void {
  // Add your logic for the "Register Student" button here
  window.location.href = '/school/register_student'
  alert('Register Student button clicked')
}

function manageSubject (): void {
  // Add your logic for the "Manage Subject" button here
  alert('Manage Subject button clicked')
}

function manageClassrooms (): void {
  // Add your logic for the "Manage Classrooms" button here
  alert('Manage Classrooms button clicked')
}

function manageAssistance (): void {
  // Add your logic for the "Manage Assistance" button here
  alert('Manage Assistance button clicked')
}

export {
  manageAssistance,
  manageClassrooms, manageSubject, registerStudent
}
