# NanoPatch

A web application for the NanoPatch system as part of an Engineering Professional Studies group project. \
This UI & API visually presents the nutrition of a plant with colour indicators as well as plotting trends of soil health over time.

> NanoPatch represents a novel stride in agricultural technology, designed as a versatile and portable system for monitoring and managing plant environments. It’s core functionality involves capturing essential environmental data around plants and displaying these insights in an accessible, user-friendly manner. NanoPatch's adaptability makes it not only a tool for economically efficient and sustainable agricultural practices but also a valuable educational resource in urban settings, where traditional farming may not be accessible.

> NanoPatch addresses the growing significance of vertical farming and its importance as a solution to farming insecurity caused by climate change. offering a solution that scales efficiently and integrates wireless data transmission accessible via a mobile device application.

<img src="NanoPatch Web App Screenshot.png" alt="Alt text" width="800"/>

## Installations

Run deployment bash script (if `dist` folder is not present) \
`./deploy.sh`

Install required packages \
`pip install -r requirements.txt`

Run NanoPatch UI Locally \
`flask run`

Top make Flask server visible to network \
`flask run --host=0.0.0.0`

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```
