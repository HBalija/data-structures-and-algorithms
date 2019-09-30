class HashTable {

  constructor(size = 53) {
    this.keyMap = new Array(size);
  }

  _hash(key) {
    let total = 0;
    const primeNumber = 31;
    for (let i = 0; i < Math.min(key.length, 100); i++) {
      const char = key[i];
      const value = char.charCodeAt(0) - 96;
      total = (total + primeNumber + value) % this.keyMap.length;
    }
    return total;
  }

  set(key, value) {
    const index = this._hash(key);
    if (!this.keyMap[index]) {
      this.keyMap[index] = [];
    }
    this.keyMap[index].push([key, value]);
  }

  get(key) {
    const index = this._hash(key);
    const indexValue = this.keyMap[index];
    if (indexValue) {
      for (const item of indexValue) {
        if (item[0] === key) return item[1];
      }
    }
    return undefined;
  }

  get values() {
    const valuesArr = [];
    for (let i = 0; i < this.keyMap.length; i++) {
      const iArray = this.keyMap[i];
      if (iArray) {
        for (let j = 0; j < iArray.length; j++) {
          if (!valuesArr.includes(iArray[j][1]))
            valuesArr.push(iArray[j][1]);
        }
      }
    }
    return valuesArr;
  }
}

const table = new HashTable(17);

table.set('indigo', '#5E84C5');
table.set('arrowtown', '#9C856D');
table.set('fuzzy wuzzy brown', '#C4405D');
table.set('Beauty Bush', '#EAB3BF');
table.set('Smoky', '#655280');
table.set('jungle green', '#2FAC9A');
table.set('polar', '#E1F9F6');
table.set('oracle', '#387A72');
table.set('atlantis', '#91C526');
table.set('hokey pokey', '##C5B826');

console.log(table.get('irish coffee'));  // undefined
console.log(table.get('fuzzy wuzzy brown'));  // #C4405D

console.log(table.values);

/*
[ '#9C856D',
  '#2FAC9A',
  '#655280',
  '#387A72',
  '#91C526',
  '##C5B826',
  '#5E84C5',
  '#E1F9F6',
  '#EAB3BF',
  '#C4405D' ]
 */
