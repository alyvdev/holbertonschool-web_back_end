import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

/**
 * Handles the profile signup process by calling signUpUser and uploadPhoto.
 * Returns an array with the settlement status of each promise.
 * @param {string} firstName - The user's first name.
 * @param {string} lastName - The user's last name.
 * @param {string} fileName - The name of the file to upload.
 * @returns {Promise<Array<{status: string, value: any}>>}
 */
function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) => results.map((result) => ({
    status: result.status,
    value:
        result.status === 'fulfilled' ? result.value : String(result.reason),
  })));
}

export default handleProfileSignup;
