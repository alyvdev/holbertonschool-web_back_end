export default class Building {
  constructor(sqft) {
    this._sqft = sqft;

    // Check if this is an instance of a subclass
    if (this.constructor !== Building) {
      // Check if the subclass has implemented evacuationWarningMessage
      if (
        this.evacuationWarningMessage === undefined
        || typeof this.evacuationWarningMessage !== 'function'
      ) {
        throw new Error(
          'Class extending Building must override evacuationWarningMessage',
        );
      }
    }
  }

  get sqft() {
    return this._sqft;
  }
}
