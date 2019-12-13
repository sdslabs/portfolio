<template>
  <div class="sister-groups w-auto flex flex-col md:content-center ml-8 mr-8 md:ml-0 md:mr-0 pt-60">
    <div class="font-black  md:self-center text-3xl leading-loose md:w-feed md:text-center">Sister Groups</div>
    <div class="font-base md:font-semibold md:self-center text-base md:text-center leading-normal md:w-sister mt-12">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor. Pellentesque sit amet augue sit amet quam feugiat porta vitae sit amet ligula.</div>
    <div class="sister flex flex-row self-center mt-32 justify-between md:w-groups">
      <div>
          <Sister v-bind:url="dsg" title="DATA SCIENCE GROUP" description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem."/>
      </div>
      <div>
          <Sister v-bind:url="pag" title="PROGRAMMING & ALGORITHMS GROUP" description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem."/>
      </div>
      <div>
          <Sister v-bind:url="infosec" title="INFOSEC IITR" description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem."/>
      </div>
    </div>
    <div class="mt-12 md:hidden"><SisterGallery/></div>
  </div>
</template>

<script>
import Sister from "@/components/about/Sister.vue";
import SisterGallery  from "@/components/about/SisterGallery.vue";
import dsg from "@/assets/images/dsg.svg";
import pag from "@/assets/images/pag.svg";
import infosec from "@/assets/images/infosec.svg";
export default {
    name: "SisterGroups",
    components: {
        Sister,
        SisterGallery
    }
}
</script>

<style lang="scss" scoped>
@media screen and (max-width: 576px) {
    .sister{
        display: none;
    }
}
</style>
