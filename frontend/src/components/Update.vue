<template>
    <div class="flex flex-col md:flex-row mt-16 mb-32">
        <div class="md:w-feed flex flex-col md:ml-60 mt-16">
            <div class="font-extrabold text-xl leading-180">{{ title }}</div>
            <div
                :class="
                    timing ? 'font-semibold text-base mt-14' : 'text-base mt-20'
                "
                class="leading-normal"
            >
                {{ timing ? timing : description }}
            </div>
            <div class="text-base mt-14 leading-normal">{{ description1 }}</div>
            <div class="text-base mt-14 leading-normal">{{ description2 }}</div>
            <div class="text-base mt-14 leading-normal">{{ description3 }}</div>
        </div>
        <div class="md:w-image">
            <img
                class="mt-12 md:mt-0 md:ml-44 md:w-image shadow-image"
                src="https://s3-alpha-sig.figma.com/img/4e0c/35b7/ecb625bceac942a2a05fc3ef05c30395?Expires=1578268800&Signature=LggaMRc8MXKlEU8Xo6-iwLVZrzX0aiz9DLCfvO21m3TEQHh39Y4XD6QLJlKYeBv8~WzEvmb4OqaP~WIvWxpKap~6kspvehR2a5ufqtaba8giP~Lkh9Y6tmfxx6lbkOtEyQwVb2kbKM-D6Doh0Nz6cIMBaGBd3yM2vWMrZ8mAYqxqPkt-u~NM9YCRdpIg9EAEIMNrTqVuETeNL4h-poR0MtskLxmg7bGch2ldQCyZS4Gz406NvqFI~HsRnvnsbfO32eH~lgygj4UqlyDBNWvUpe6NgTFVdbzmXDT4uc9~uwln1xwwQcLViJ5bOv3G73Sxhp1ndVxe6D5DyAvEGaHCOw__&Key-Pair-Id=APKAINTVSUGEWH5XD5UA"
            />
        </div>
    </div>
</template>

<script>
export default {
    name: "update",
    props: {
        title: String,
        timing: String,
        description: String,
        description1: String,
        description2: String,
        description3: String,
        url: String
    }
};
</script>
