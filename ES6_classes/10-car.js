export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Using Symbol.species to ensure the correct constructor is used when cloning
  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species();
  }
}
