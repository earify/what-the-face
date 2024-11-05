console.log(faceapi)

const run = async()=>{
    await Promise. all([
        faceapi.nets. ssdMobilenetv1. loadFromUri('./models'),
        faceapi.nets. faceLandmark68Net. loadFromUri('./models'),
        faceapi.nets. faceRecognitionNet.loadFromUri('./models'),
        faceapi.nets. ageGenderNet. loadFromUri('./models'),
    ])

    const face1 = document.getElementById('face')
    let faceAIData = await faceapi.detectAllFaces(face1).withFaceLandmarks().withFaceDescriptors().withAgeAndGender()
    console.log(faceAIData)

    const canvas = document.getElementById('canvas')
    canvas.style.left = face1.offsetLeft
    canvas.style.top = face1.offsetTop
    canvas.height = face1.height
    canvas.width = face1.width

    faceAIData = faceapi.resizeResults(faceAIData, face1)
    faceapi.draw.drawDetections(canvas, faceAIData)
}

run()