/**
 * App controller class
 */
class AppController {
  /**
   * Get homepage handler
   * @param {Object} request - Express request object
   * @param {Object} response - Express response object
   */
  static getHomepage(request, response) {
    response.status(200).send('Hello Holberton School!');
  }
}

export default AppController;
