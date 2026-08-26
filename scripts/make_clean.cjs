const fs = require('fs');
let html = fs.readFileSync('/Users/mihyunlee/나는 1인기업 대표/코부장 프로젝트/움직이는그림사전/_작업/복사기.html', 'utf8');
let matches = [...html.matchAll(/<p>(.*?)<\/p>/g)];
let prompts = matches.map(m => m[1].replace(/&quot;/g, '"').replace(/&#39;/g, "'"));
fs.writeFileSync('/Users/mihyunlee/나는 1인기업 대표/코부장 프로젝트/움직이는그림사전/_작업/벌크입력/벌크_04_엔터전용.txt', prompts.join('\n'));
