import { uploadPhoto, createUser } from './utils';

/**
 * Asynchronously uploads a photo and creates a user.
 * Returns an object containing the responses from both operations.
 * If either operation fails, returns an object with null values.
 * @returns {Promise<{photo: any, user: any}>}
 */
export default async function asyncUploadUser() {
  try {
    const [photoResponse, userResponse] = await Promise.all([
      uploadPhoto(),
      createUser(),
    ]);
    return {
      photo: photoResponse,
      user: userResponse,
    };
  } catch (error) {
    return {
      photo: null,
      user: null,
    };
  }
}
