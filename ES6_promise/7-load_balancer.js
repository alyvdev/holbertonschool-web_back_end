/**
 * Returns the value of the first promise to resolve.
 * @param {Promise} chinaDownload - A promise representing a download from China.
 * @param {Promise} USDownload - A promise representing a download from the US.
 * @returns {Promise<any>} A promise that resolves with the value of the first resolved promise.
 */
export default function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([chinaDownload, USDownload]);
}
