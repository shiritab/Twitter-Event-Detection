<template>
    <div id="markdownHtml" style="text-align: left; margin: 50px;"></div>
</template>

<script>
var marked = require('marked');

export default {
  name: "HelpPage",
  data() {
    return {
      readme: "",
      markdownHTML: "",
      body: null,
    }
  },
  methods: {
    async getMarkdownHTML() {
      /* Get request for markdown file as html string and require all imgs in it. 
      Then save to this.body */

      const htmlResponse = await this.axios.get(`${this.$root.serverLink}/files/markdown`);
      this.readme = htmlResponse.data;
      document.getElementById("markdownHtml").innerHTML = this.readme;
      const el =  document.getElementById("markdownHtml");
      let imgs = this.getImgs(el);

      imgs.forEach((img) => {
        let source = img[0].src;
        img[0].src = require(`../../${source.substring(source.indexOf("assets"))}`);
        img[0].className = "image";
      });

      this.body = el.body;
    },

    getImgs(el) {
      /** Given html element get all imgs in p tags and save to imgs list. */
      let imgs = [];
      const paragraphs = el.getElementsByTagName("p");

      for (let index = 0; index < paragraphs.length; index++){
        const p = paragraphs[index];
        let img = p.getElementsByTagName("img");
        if (img.length > 0){
          imgs.push(img);
        }
      };

      return imgs;
    }
  },
  created() {
    console.log(`Created HelpPage`);
    this.getMarkdownHTML();
  }
}
</script>

<style>
.image{
  width: 30%;
}
</style>

