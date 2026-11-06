---
id: "javascript_045"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 45
source_url: "https://developer.mozilla.org/en-US/blog/image-formats-pixels-graphics"
language: "en"
retrieved_at: "2026-11-01 21:52:39"
content_hash: "486af5855d508b425de7e88145a9d04d5be626592d86dd08dfb35c4f94b91f0e"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/image-formats-pixels-graphics

---

# Image formats: Pixel data from encoders to decoders

[In the previous post](https://developer.mozilla.org/en-US/blog/color-models-humans-devices/), we focused on how images are seen by people and shown on devices.
Now it's time to zoom in and explore the tiny building blocks of an image â the pixels and the bytes behind them.

## [What is an image pixel?](https://developer.mozilla.org#what_is_an_image_pixel)

To display an image, a device needs to get information about the colors of different parts of the image from a data source. For a device, most images are just grids, and each cell in that grid is a pixel. A pixel is an ephemeral value; it doesn't have a size or shape. It's up to the hardware and software to decide how to represent these pixels.

There are an infinite number of ways to store pixel data, so devices need to understand the image format, that is, the way that data is organized.
On the web, there are [several common formats](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types#common_image_file_types): JPEG, AVIF, WebP, JPEG XL, PNG and many others.
Pixels have a few important properties:

- They're arranged in a grid to form an image, and the order matters.
- Each pixel holds [color and luminance](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Colors_and_Luminance) information.
These values are discrete and limited by the number of bits defined by the image format.

**Note:**
AVIF can use 8, 10, or 12 bits to store pixel data.
A newer JPEG format, JPEG XL, supports up to 32 bits per color channel.
The most common setup is 8 bits per channel, with values ranging from 0 to 255.
That gives only 256 possible "shades" for each color component â and 256 Ã 256 Ã 256 â 16 million possible colors in total.

It's important to know the difference between **image pixels** and **device pixels**.
Image pixels are part of image data, while [device pixels](https://developer.mozilla.org/en-US/docs/Glossary/Device_pixel) are physical pixels that depend on the display.
The way device pixels work can vary: for example, in OLED screens, each pixel is a tiny light-emitting diode; in LCDs, it's a crystal controlled by a backlight; and in e-ink displays, it's made up of charged particles that move to form the image.

## [Images in your graphics card](https://developer.mozilla.org#images_in_your_graphics_card)

For a display to show an image, the video card needs to send that image as a signal to the display. A simplified explanation is that the graphics card stores the image pixel data as an array of numbers. Let's look at how to manipulate pixel data in JavaScript:

```
<div class="symbols-holder"></div>
```
```
.symbols-holder {
  font-family: monospace;
  white-space: pre;
  font-size: 5px;
  line-height: 3px;
}
```
```
const imageToSymbols = (src, showPixelsSomehow) => {
  const img = new Image(); // create an image element
  img.onload = () => {
    const width = 128;
    const height = 128;
    const canvas = new OffscreenCanvas(width, height);
    const ctx = canvas.getContext("2d");
    ctx?.drawImage(img, 0, 0);
    const resp = ctx.getImageData(0, 0, width, height); // read image data
    let str = "";
    // convert image data to string
    for (let i = 0; i < resp.data.length; i += 4) {
      // use opacity channel
      str += resp.data[i + 3] > 255 / 2 ? "*" : ".";
      if (i % (4 * width) === 0) {
        str += "\n";
      }
    }
    showPixelsSomehow(str);
  };
  img.src = src;
};
imageToSymbols("squirrel.png", show);
```
The extracted [`ImageData`](https://developer.mozilla.org/en-US/docs/Web/API/ImageData) is a contiguous [typed array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays) of unsigned 1-byte integers.
In the example, the image doesn't contain any color.
Instead, each image pixel has [four components](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#srgb), and all the interesting information is stored in the fourth one â the alpha channel.
By reading every fourth element, we can scan the entire image through the alpha channel.

**Note:**
The alpha channel stores information about image transparency.
A value of `255` means the pixel is fully opaque, while `0` means it's fully transparent.

## [Image specification](https://developer.mozilla.org#image_specification)

As an example, let's look at a very small image that's 100Ã133 pixels:

If there's no alpha channel â meaning each pixel has only three components â and we use 8-bit color, the raw size of the image should be around 40â¯KB. But the actual file is less than 3â¯KB. Soon it will be clear why. For larger images, this difference becomes even more significant.

Now imagine that instead of a single image, a short 60-second video needs to be rendered. With 24 frames per second, that results in 1,440 frames. At 38 KB per frame, the total size would be around 55 MB. Obviously, there's a need to pack pixels efficiently. To handle this, many image and video formats have been developed: BMP, GIF, JPEG, PNG, JPEG2000, several versions of MPEG, H.264, VP8, VP9, and AV1.

So the data gets encoded first and decoded later â the thing that handles this is called a [*codec*](https://developer.mozilla.org/en-US/docs/Glossary/Codec) (en**co**ded, **dec**oded).
Encoding can happen on either the CPU or GPU.
Usually, image data sits in RAM, the CPU decodes it, and the result gets sent to the GPU so it can be shown on the screen.
But when things get heavier â like with video playback â it's more efficient to upload the compressed image data instead.
In that case, the GPU does the decoding itself.

A video is made up of two types of frames: intraframes and interframes. Intraframes are basically full images that get compressed, while interframes store information about how parts of the image move from one frame to the next.

**Note:**
More accurately, interframes contain [motion vectors](https://en.wikipedia.org/wiki/Motion_estimation).

Intraframe compression works just like image compression. Formats like AVIF, HEIF, and WebP are actually based on the intraframe compression used in related video codecs. In general, codecs evolve faster than image formats, so image formats often end up as a side product of video codec development.

For example, back when modern image formats weren't widely supported by browsers (which isn't the case anymore), one-frame videos were used instead of images.

## [How image encoders work](https://developer.mozilla.org#how_image_encoders_work)

The sequence of bits generated by the encoder is called a bitstream.
To transfer or store this data, it needs to be split into chunks.
These chunks have different names depending on the format.
For example, in AV1 video and AVIF images, they're called *OBUs* (Open Bitstream Units).
Each unit has its own structure so the decoder knows what to do with it.

But an image is usually more than just a sequence of bitstream units.
As mentioned earlier, it can also include an ICC profile and other metadata â like image dimensions, color space, camera settings, date, time, and location.
All of this needs to be packed into a *container*.

Containers have their own specifications, and different media formats can reuse the same container. For example:

- AVIF is an AV1 bytestream in a HEIF container.
- WebP is a VP8 bytestream (or lossless WebP) in a RIFF container.

Sometimes, an image format defines its own container. PNG, JPEG, and JPEG XL include the layout as part of the file format specification.

## [How image decoders work](https://developer.mozilla.org#how_image_decoders_work)

A decoder figures out the format by reading the beginning of the file, which usually contains a *magic number* â a few bytes that identify the format.
For AVIF, this magic number is `ftypavif`.

Then it follows the container layout to find the relevant data. Usually, the metadata comes first, then the actual bytestream. Let's see how this works with some squirrel images ð

The image contains a lot of metadata at the beginning of the file:

width: 1536
height: 1536
bands: 3
format: uchar
coding: none
interpretation: srgb
xoffset: 0
yoffset: 0
xres: 2.83465
yres: 2.83465
filename: ./squirrel.jpg
vips-loader: jpegload
jpeg-multiscan: 1
interlaced: 1
jpeg-chroma-subsample: 4:2:0

It's fine if most of this doesn't make sense yet â some of these entries will be explained later. As you can see, the width and height are stored at the beginning of the container. That's especially useful for browsers, which can quickly allocate space on the page for the image.

**Note:**
Don't make the browser figure out the image's height and width â that can cause nasty layout shifts.
Instead, set the `width` and `height` attributes on the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img) element.

## [Taking a deeper look at encoders](https://developer.mozilla.org#taking_a_deeper_look_at_encoders)

So how can an encoder squeeze the 38â¯KB of image data into just 3â¯KB? Encoders use a bunch of techniques and algorithms that take advantage of how we perceive images and how images are structured. Let's go through them one by one.

### [Lossy and lossless compression methods](https://developer.mozilla.org#lossy_and_lossless_compression_methods)

There are two ways to compress an image:

- **Lossy:** The encoded image will change or remove some information along the way and is no longer identical to the original.
- **Lossless:** The image can be fully reconstructed.

Lossy and lossless compression methods can be combined, which can sometimes provide better results with fewer bytes. For example, the alpha channel (which controls opacity) can be compressed losslessly, while the color channels use lossy compression for better efficiency.

The table below summarizes several popular image formats:

| Format | Compression type | Notes | 
|---|---|---|
| PNG | Lossless | Always lossless | 
| JPEG | Lossy | Always lossy | 
| WebP | Hybrid | Can be a lossy VP8 frame or lossless using a different algorithm | 
| AVIF | Lossy or lossless |  | 
| JPEG XL | Lossy or lossless |  | 

### [Chroma subsampling](https://developer.mozilla.org#chroma_subsampling)

Humans are much more sensitive to luminance than to color. The YCbCr color space takes advantage of this fact by separating brightness (luminance) from color information, which allows for more efficient compression.

Instead of storing the full color details of every pixel, the encoder skips some of the color data.
The decoder then reconstructs it based on the colors of nearby pixels.
This technique is called [chroma subsampling](https://en.wikipedia.org/wiki/Chroma_subsampling).

Chroma subsampling is described using three numbers that correspond to a 4Ã2 pixel grid:

- The first number is always 4 and represents the width of the region.
- The second number shows how many chroma samples (Cb and Cr) are stored in the first row.
- The third number shows how many chroma samples are stored in the second row.

AVIF supports the following chroma subsampling formats:

- **4:4:4** â No subsampling; all color information is preserved.
- **4:2:2** â Half of the color information is discarded.
- **4:2:0** â Only a quarter of the original color data is kept.

This is an example of a lossy transformation. Once applied, the original image can't be fully restored, but it still looks pretty good to a viewer while saving storage and bandwidth.

### [Exploiting spatial locality](https://developer.mozilla.org#exploiting_spatial_locality)

Let's look at a code example to demonstrate the next technique. There are two canvases: one with random pixels and another with a solid color.

```
const width = 100;
const height = 100;
let ctx = canvas1.getContext("2d");
for (let i = 0; i < width; i++) {
  for (let j = 0; j < height; j++) {
    ctx.fillStyle = `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${
      Math.random() * 255
    })`;
    ctx.fillRect(i, j, 1, 1);
  }
}
ctx = canvas2.getContext("2d");
ctx.fillStyle = "rgba(6, 142, 110, 0.81)";
ctx.fillRect(0, 0, width, height);
```
Try saving both images separately: right-click each and choose "Save Image As". Even with a not-so-efficient browser codec, the first image will be around 35â¯KB, while the second one will be just 500 bytes. That's a 70x difference in size!

The reason is that there's no relationship between the pixels in the first image.
In real images, neighboring pixels are usually related in some way.
They might share the same color, form a gradient, or follow a pattern.
This property is called *spatial locality*.

The less [information](<https://en.wikipedia.org/wiki/Entropy_(information_theory)>) an image has, the better it can be compressed.
Codecs take full advantage of this property and divide the image into regions and compress each region separately.

For example, JPEG always splits the image into 8Ã8 blocks. More modern image formats allow flexible block sizes. AVIF, for instance, uses blocks ranging from 4Ã4 to 128Ã128. Codecs typically stick to power-of-two block sizes to keep calculations simple and efficient.

For an image with a solid blue sky, it's more efficient to divide that area into larger blocks, which reduces the need to store unnecessary detail. The same rule applies to any solid background. But how does the encoder decide where and how to split an image? There are several techniques for this, which we can explore next.

AVIF uses a recursive approach to partition the image into blocks.
It starts by splitting the image into larger blocks called *superblocks*.
Then, it analyzes the content of each block and decides whether to split it further or keep it as is.
To manage this partitioning, AVIF uses a *quadtree* data structure.
Quadtrees are also commonly used in map applications to store locations and efficiently find nearby objects.

You can build a quadtree yourself by recursively splitting the image into four squares. For every square, calculate the mean color and the deviation from the mean. If the deviation is too high, split the square again.

```
function buildQuadtree(params) {
  const { x, y, w, h, forceSplitSize, minSize, threshold, data, totalWidth } =
    params;
  // always split big regions
  const forced = w > forceSplitSize && h > forceSplitSize;
  const std = regionStd(x, y, w, h, data, totalWidth);
  // if the region is too small or color varies little, stop
  if (w <= minSize || h <= minSize || (!forced && std < threshold)) return;
  ctx.strokeRect(x, y, w, h);
  const midW = (w / 2) | 0;
  const midH = (h / 2) | 0;
  if (midW === 0 || midH === 0) return;
  const nextParams = { ...params, w: midW, h: midH };
  // left top
  buildQuadtree({ ...nextParams });
  // right top
  buildQuadtree({ ...nextParams, x: x + midW, y });
  // left bottom
  buildQuadtree({ ...nextParams, x, y: y + midH });
  // right bottom
  buildQuadtree({
    ...nextParams,
    x: x + midW,
    y: y + midH,
  });
}
function showSplit(imgData, totalWidth) {
  const params = {
    threshold: 28,
    minSize: 8,
    forceSplitSize: 128,
    totalWidth,
  };
  buildQuadtree({
    x: 0,
    y: 0,
    w: totalWidth,
    h: totalWidth,
    data: imgData.data,
    ...params,
  });
}
```
### [Prediction modes](https://developer.mozilla.org#prediction_modes)

The less data a block contains, the better it can be compressed. Try playing with an 8Ã8 pixel block by clicking different cells on the canvas below. After a few clicks, a part of the pattern marked in green will be reproduced.

Instead of storing every pixel in a grid, space can be saved by storing only the differences between the actual image and the closest matching pattern.

Modern image codecs use the same idea.
They predict a basic structure for each block, then compress only the differences, called *residuals*, between the actual block content and the prediction.

Most images have some underlying structure, and codecs take advantage of this by analyzing patterns like gradients or repeating textures to make better predictions.

Pixels inside a block often form a pattern related to their neighboring values. So instead of using static patterns, codecs use the top row and left column of the block as references to make a prediction. Take the left example in the image: the pixels inside the square closely resemble some of the surrounding pixels.

Different codecs use various *prediction modes* to find the best way to represent this structure and minimize the error.
For example:

- The block can be predicted as an average of its neighboring pixels.
- It can repeat pixels in specific directions (as shown in the picture).
- It might combine multiple neighboring pixels to create a more accurate prediction.
- More advanced predictors take the coordinates of each pixel within the block into account to refine the result.
- Even more advanced modes go further by recursively predicting pixels from previous rows and columns. Instead of relying only on reference pixels, the encoder generates patches using previously predicted pixels.

By improving these predictions, codecs can significantly reduce the amount of data that needs to be stored or transmitted. For example, one of AVIF's prediction modes is based on the left neighbor reference pixel, the top-right reference pixel, and the pixel's coordinates within the block.

Predictions aren't limited to spatial structure â color channels can be connected too.
This idea is used in both AVIF and JPEG XL.
The related prediction mode, *chroma from luma*, predicts the color channels (UV) based on information from the corresponding Y (luminance) channel.
Some codecs, instead of predicting pixels, can store an instruction to copy the content of another block.
This is particularly useful for screenshots or images with repetitive patterns because it reduces redundancy.

The number of prediction modes varies between codecs. AVIF has many (71), WebP has fewer (10), and JPEG doesn't use prediction at all.

### [Block transformations](https://developer.mozilla.org#block_transformations)

The codec makes a prediction and then finds pixel differences from that prediction. Next, the codec needs to store these differences efficiently, and that's when it's time to throw away some data, that is, apply a lossy transformation.

You can think of it using the same pattern analogy. Now there's a fixed set of patterns, and the goal is to figure out the best way to combine them to get something close to the original block. It's like building an image by stacking multiple layers, each with different opacities â each layer contributes to the final result, and the trick is to guess the right opacity for each one. The math that makes this work is called the Discrete Cosine Transform (DCT).

Why does this help reduce file size? Humans are less sensitive to high-frequency components, such as tiny dots or fine textures. The transformation separates these high and low-frequency parts, making it easier to decide which details can be safely discarded.

A well-known way to visualize this is through *DCT basis functions*, which show how different frequency components contribute to an image.

**Note:**
While this is a useful illustration, keep in mind that modern codecs apply the transformation to *residuals*, not the original image.

Let's see how this works with an example. Imagine an 8Ã8 block that has a horizontal 2-pixel-thick line running across the center:

```
.out {
  font-family: monospace;
  white-space: pre;
}
```
```
const block = [
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 1, 1], // <- line
  [1, 1, 1, 1, 1, 1, 1, 1], // <- line
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
];
// special weight function
const alpha = (u, size) =>
  u === 0 ? 1 / Math.sqrt(size) : Math.sqrt(2 / size);
// A very naive and innefficient implementation of 2D DCT
const dct2D = (block) => {
  const size = block.length;
  // create block of the same size
  const result = Array.from({ length: size }, () => Array(size).fill(0));
  // apply DCT formula
  for (let u = 0; u < size; u++) {
    for (let v = 0; v < size; v++) {
      let sum = 0;
      for (let x = 0; x < size; x++) {
        for (let y = 0; y < size; y++) {
          sum +=
            block[x][y] *
            Math.cos(((2 * x + 1) * u * Math.PI) / (2 * size)) *
            Math.cos(((2 * y + 1) * v * Math.PI) / (2 * size));
        }
      }
      result[u][v] = alpha(u, size) * alpha(v, size) * sum;
    }
  }
  return result;
};
```
Of course, the actual implementations are efficient and optimized:

- Instead of applying DCT to the whole block at once, codecs use two 1D DCTs first on the rows, then on the columns.
- Some codecs support alternative transforms.
For example, AVIF can use a [sine transform](https://en.wikipedia.org/wiki/Discrete_sine_transform) instead of DCT.
- Codecs use fast algorithms like the [butterfly-based fast DCT](https://en.wikipedia.org/wiki/Butterfly_diagram).
- Transform steps are optimized for vector operations using SIMD instructions, which let the CPU apply the same operation to multiple values with one command.
- The DCT can also be performed directly on the GPU. The AV1 codec (which AVIF is based on) supports this.

In more advanced codecs, the transform can be applied to parts of a block rather than the whole thing. AVIF, for example, allows a block to be subdivided (up to two times) into smaller blocks, with transforms applied separately to each sub-block.

At this stage, a small lossy error is introduced due to rounding in floating-point calculations. But this step alone doesn't reduce the file size much.

### [Quantization](https://developer.mozilla.org#quantization)

To prepare the image for compression, codecs convert the float coefficients into integers and divide each one by a specific number.
The goal is to get as many zeros as possible after division â less data means better compression.
These numbers are known as *quantization parameters*.

A popular set of quantization values used in JPEG looks like this:

These parameters are different for luminance and color channels.

Quantization parameters are stored in the image container, and for JPEG, quality is determined by how we scale those parameters. The bigger the coefficients, the more zeros we get after applying them.

In more advanced codecs, the process is much more complex. Specialized algorithms are used to properly round the results of quantization. Additionally, different quantization parameters can be applied to different sets of blocks, allowing the quality to vary across different parts of the image.

### [Bonus: interlacing](https://developer.mozilla.org#bonus_interlacing)

Since different coefficients represent different levels of detail, it's possible to get interlacing (also known as progressive rendering) almost for free. To do this, the coefficients are reordered so that the ones with coarse (basic) details are stored (and loaded) first.

As a result, the image is built up in multiple layers of detail, called *scans*.
The first scan shows a rough, usually blurry version of the image.
Each following scan adds more detail, step by step.

For most image formats, this reordering doesn't increase the file size, so it's a useful trick. But be careful with interlaced PNGs â they use a different method that does increase file size.

### [Entropy coding](https://developer.mozilla.org#entropy_coding)

Now we approach the final step, and it's time to explain why plain color images are so small compared to random noise.
The reason is *entropy coding*.

After the codec gets the quantized coefficients, the next step is to shrink the binary size as much as possible.
The block's coefficients are scanned in a zigzag order, and the resulting sequence is encoded using an algorithm from the [entropy coding family](https://en.wikipedia.org/wiki/Entropy_coding).
The idea is simple: use fewer bits for values that appear more often.

Let's try coding a basic version ourselves. Suppose we have this string of numbers:

124 124 124 124 10 123 123 1 1 2

The first step is to count how often each number appears in the sequence.

```
const vals = "124 124 124 124 10 123 123 1 1 1 2"
  .split(" ")
  .map((e) => parseInt(e, 10));
// count how many times each value appears
const groups = Object.groupBy(vals, (e) => e);
// sort the result, most frequent first
const freqs = Object.entries(groups)
  .map(([key, value]) => [key, value.length])
  .sort((a, b) => b[1] - a[1]);
```
Now we can assign the shortest binary code to the most frequent value, like this:

124 - 0
1 - 10
123 - 110
2 - 1110
10 - 1111

And we can encode the string using only 24 bits instead of 88 bits `000011111101101010101110` ð.
This is how JPEG achieves compression.
The algorithm used is called [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding).

Some codecs use more advanced algorithms like [arithmetic coding](https://en.wikipedia.org/wiki/Arithmetic_coding) or [asymmetric numeral systems](https://en.wikipedia.org/wiki/Asymmetric_numeral_systems).
Arithmetic coding allows compression to come closer to the theoretical limit, achieving a higher compression rate compared to Huffman coding.

**Note:**
This limit is defined by the [Shannon entropy](<https://en.wikipedia.org/wiki/Entropy_(information_theory)>) of the data.
It represents the minimum number of bits needed to encode that data.

### [Post-processing](https://developer.mozilla.org#post-processing)

Lossy compression introduces various artifacts because it removes high-frequency components. This can lead to several visible effects, such as:

- Blocking â visible square-shaped patterns, especially in flat areas
- Blurry edges
- Color distortions â inaccurate or shifted colors
- Ringing â halos or echo-like patterns around edges
- Mosquito noise â small flickering dots or buzzing around edges

To reduce these artifacts, some encoders add post-processing filters. These filters are applied by the decoder when reconstructing the image pixels. The filter settings are stored in the bytestream, so the decoder can read and apply them during decoding.

You might remember the old trick of applying a [Gaussian blur](https://en.wikipedia.org/wiki/Gaussian_blur) to an image to reduce noise.
This is a similar idea, but modern codecs use more advanced algorithms.

- Deblocking filters â for example, Gabor filters used in JPEG XL
- Wiener filter â used in AV1 to reduce noise
- CDEF (Constrained Directional Enhancement Filter) â helps reduce ringing artifacts

Typically, if several filters are used, they form a pipeline with an exact order of application. For example, CDEF is applied after the deblocking filter.

## [Wrapping up](https://developer.mozilla.org#wrapping_up)

In this post, we explored how image encoding works, how it's connected to human perception, and how decoding reconstructs the image from bits. Most codecs follow the same core ideas, but they use different methods and techniques. They support more block sizes, extra prediction modes, various types of transforms, different coding algorithms, and often include a post-processing pipeline to polish the final image.

The obvious takeaway is that modern codecs are more complex (and sometimes slower), but they usually produce better results. However, "better" isn't always easy to define. Some questions still remain: what are the trade-offs between codec complexity and output quality? And which codecs work best in different situations?