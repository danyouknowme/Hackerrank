'use strict';

import { WriteStream, createWriteStream } from "fs";
process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on('data', function(inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on('end', function(): void {
    inputLines = inputString.split('\n');
    inputString = '';

    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}

/*
 * Complete the 'equalizeArray' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function equalizeArray(arr: number[]): number {
    // Write your code here
    let obj: { [n: number]: number } = {};
    let key: number;
    let max = 0;
    const length = arr.length;
    arr.forEach((item) => {
        key = item;
        (key in obj) ? obj[key]++ : obj[key] = 1;
    });
    for (let prop in obj) {
        (obj[prop] > max) && (max = obj[prop]);
    }
    return length - max;
}

function main() {
    const ws: WriteStream = createWriteStream(process.env['OUTPUT_PATH']);

    const n: number = parseInt(readLine().trim(), 10);

    const arr: number[] = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const result: number = equalizeArray(arr);

    ws.write(result + '\n');

    ws.end();
}
