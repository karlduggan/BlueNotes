<template>
<div class="container">
    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="50px" height="50px" viewBox="-10 -10 600 450" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:1.5;">
    <g transform="matrix(1,0,0,1,-507.833,-1330.83)">
        <g transform="matrix(0.92555,0,0,0.870355,38.1184,227.389)">
            <path d="M615,1625L615,1753.94L743.937,1625L1036.01,1625L1036.01,1272.6L512,1272.6L512,1625L615,1625Z" stroke="green" stroke-width="30" fill="transparent"/>
        </g>
    </g>
</svg>
</div>
</template>

<script>
export default {
    name: 'CommentButton',
    props: {
        'background-color': String,
        'stroke-color': String,
        'nummberOfCommments':String
    }

}
</script>
<style lang="scss" scoped>
.container {
    position: absolute;

}
.container:hover {
    cursor: pointer;
}
</style>