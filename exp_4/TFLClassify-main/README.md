# 基于TensorFlow Lite实现的Android花卉识别应用

## 向应用中添加TensorFlow Lite
![4 U3HW6SMF76I@BZ}_0RNIE](https://github.com/Jarrod030/AS_ML/assets/74969760/27d480c0-3523-4fd4-bbca-5f1947a0d10b)

## 添加代码重新运行APP

定位“start”模块MainActivity.kt文件的TODO 1，添加初始化训练模型的代码

```
private class ImageAnalyzer(ctx: Context, private val listener: RecognitionListener) :
        ImageAnalysis.Analyzer {

  ...
  // TODO 1: Add class variable TensorFlow Lite Model
  private val flowerModel = FlowerModel.newInstance(ctx)

  ...
}
```

在CameraX的analyze方法内部，需要将摄像头的输入ImageProxy转化为Bitmap对象，并进一步转化为TensorImage 对象

```
override fun analyze(imageProxy: ImageProxy) {
  ...
  // TODO 2: Convert Image to Bitmap then to TensorImage
  val tfImage = TensorImage.fromBitmap(toBitmap(imageProxy))
  ...
}

```

按照属性score对识别结果按照概率从高到低排序
列出最高k种可能的结果，k的结果由常量MAX_RESULT_DISPLAY定义

```
override fun analyze(imageProxy: ImageProxy) {
  ...
  // TODO 3: Process the image using the trained model, sort and pick out the top results
  val outputs = flowerModel.process(tfImage)
      .probabilityAsCategoryList.apply {
          sortByDescending { it.score } // Sort with highest confidence first
      }.take(MAX_RESULT_DISPLAY) // take the top results

  ...
}
```

将识别的结果加入数据对象Recognition 中，包含label和score两个元素。后续将用于RecyclerView的数据显示

```
override fun analyze(imageProxy: ImageProxy) {
  ...
  // TODO 4: Converting the top probability items into a list of recognitions
  for (output in outputs) {
      items.add(Recognition(output.label, output.score))
  }
  ...
}
```

将原先用于虚拟显示识别结果的代码注释掉或者删除

```
// START - Placeholder code at the start of the codelab. Comment this block of code out.
for (i in 0..MAX_RESULT_DISPLAY-1){
    items.add(Recognition("Fake label $i", Random.nextFloat()))
}
// END - Placeholder code at the start of the codelab. Comment this block of code out.
```

##运行结果

![XXN05RCGZ}6QHM5D1NCGX4W](https://github.com/Jarrod030/AS_ML/assets/74969760/36efe176-6aa6-458e-b399-ae12b3438b09)
