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
 * Complete the 'permutationEquation' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY p as parameter.
 */

function jumpingOnClouds(c: number[], k: number): number {
    let point: number = 0;
    let energy: number = 100;
    while (true) {
        point = (point + k) % c.length;
        (c[point] === 1) ? energy -= 3 : energy -= 1;
        
        if (point === 0) {
            break;
        }
    }
    return energy;
}

function main() {
    const fs: WriteStream = createWriteStream(process.env['OUTPUT_PATH']);

    const nk = readLine().split(" ");
     
    const n: number = parseInt(nk[0], 10);
    
    const k: number = parseInt(nk[1], 10);
    
    const c: number[] = readLine().split(' ').map(cTemp => parseInt(cTemp, 10));
    
    let result: number = jumpingOnClouds(c, k);
    
    fs.write(result + "\n");

    fs.end();
}
