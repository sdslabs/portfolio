<template>
  <div class="sister-groups flex flex-col content-center w-full">
    <div class="font-black self-center text-3xl leading-loose w-feed text-center">Sister Groups</div>
    <div class="font-semibold self-center text-base text-center leading-normal w-sister mt-16">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor. Pellentesque sit amet augue sit amet quam feugiat porta vitae sit amet ligula.</div>
    <div class="flex flex-row self-center mt-32 justify-between w-groups">
      <div>
          <Sister url="" title="DATA SCIENCE GROUP" description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem."/>
      </div>
      <div>
          <Sister url="" title="PAG" description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem."/>
      </div>
      <div>
          <Sister url="" title="INFOSEC IITR" description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem."/>
      </div>
    </div>
  </div>
</template>

<script>
import Sister from "@/components/about/Sister.vue"
export default {
    name: "sisterGroups",
    components: {
        Sister
    }
}
</script>
