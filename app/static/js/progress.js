

// function uploadProgress(){
//     var xhr = new window.XMLHttpRequest();
//     xhr.upload.addEventListener('progress',function(event){
//         if(event.lengthComputable){
//             console.log('Bytes Loaded: '+event.loaded);
//             console.log('total size'+event.total);
//             console.log('Percentage Uploaded' + (event.loaded / event.total)*100);

//             var percent = Math.round((event.loaded / event.total)*100);
//             $('#progressBar').attr('aria-valuenow',percent).css('width',percent+'%').text(percent+'%');
//         }
//     });

//     return xhr;
// }


// $(document).ready(function() {
//     $('form').on('submit',function(event){
//         $('#loading-stuff').removeClass('d-none')
//         // event.preventDefault();

//         var formData = new FormData($('form')[0]);

//          $.ajax({
//             xhr: uploadProgress,
//             type: 'POST',
//             url: '/create_post',
//             data: formData,
//             processData: false,
//             contentType: false,
//             success: function(){
//                 $('#progressBar').attr('aria-valuenow',0).css('width',0+'%').text('');
//                 $('#loading-stuff').addClass('d-none');
//                 console.log("Doneeeeeeeee")
//             }
//         })
//         console.log(formData)

//         $("#cancel-button").button().click(function() {
//             console.log("Canelinggggggg");
//             xhr.abort();
//         });
//     })
// })
