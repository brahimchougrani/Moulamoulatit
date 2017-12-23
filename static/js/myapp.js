/**
 * Created by pc on 17/12/17.
 */
$(document).ready(function () {
    $('.carousel').carousel();
     function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#image_upload_preview').attr('src', e.target.result);
            };

            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#id_image").change(function() {
      readURL(this);
    });
        if($('#wrapper2 .formset_row').length===0){
                j = 0;
            }else{
                j = $('#wrapper2 .formset_row').length-1;
            }
        $("#costum_fs2").click(function(){
            j++;
            $("#id_imageupload_set-TOTAL_FORMS").attr("value",j+1);
            $("#wrapper2 ").append('' +
                '<div class=" formset_row">'+
                        '<input type="file" name="imageupload_set-'+j+'-relationship" id="id_imageupload_set-'+j+'-relationship">' +
                        '<input type="hidden" name="imageupload_set-'+j+'-bld" id="id_imageupload_set-'+j+'-bld">'+
                        '<input type="hidden" name="imageupload_set-'+j+'-id" id="id_imageupload_set-'+j+'-id">'+
                        '<div> '+
                            '<input type="hidden" name="imageupload_set-'+j+'-x" id="id_imageupload_set-'+j+'-x" step="any">'+
                            '<input type="hidden"  name="imageupload_set-'+j+'-y" id="id_imageupload_set-'+j+'-y" step="any">'+
                            '<input type="hidden"  name="imageupload_set-'+j+'-width" id="id_imageupload_set-'+j+'-width" step="any">'+
                            '<input type="hidden"  name="imageupload_set-'+j+'-height" id="id_imageupload_set-'+j+'-height" step="any">'+
                        '</div>'+
                        '<div><input type="checkbox"  name="imageupload_set-'+j+'-DELETE" id="id_imageupload_set-'+j+'-DELETE"></div>'+

                '</div>'
            );
        });
        if($('#wrapper .formset_row').length===0){
                i = 0;
            }else{
                i = $('#wrapper .imgnum').length-1;
            }
        $("#costum_fs").click(function(){
            i++;
            $("#id_circtuidetail_set-TOTAL_FORMS").attr("value",i+1);
            $("#wrapper").append('' +
                '<hr>'+
                '<div class="imgnum">'+
                    '<div>' +
                        '<label for="id_circtuidetail_set-'+i+'-Circuit">Titre circuit </label>'+
                        '<input type="hidden" name="circtuidetail_set-'+i+'-Circuit" id="id_circtuidetail_set-'+i+'-Circuit"> ' +
                        '<input type="hidden" name="circtuidetail_set-'+i+'-id" id="id_circtuidetail_set-'+i+'-id">' +
                        '<input type="text" name="circtuidetail_set-'+i+'-titre_circuit" id="id_circtuidetail_set-'+i+'-titre_circuit" maxlength="255">' +
                    '</div>'+
                    '<div>'+
                        '<label for="id_circtuidetail_set-'+i+'-Description">Description </label>'+
                       '<textarea name="circtuidetail_set-'+i+'-Description" rows="10" id="id_circtuidetail_set-'+i+'-Description" cols="40"></textarea>'+
                    '</div>'+
                    '<div>'+
                        '<label for="id_circtuidetail_set-'+i+'-DELETE">Supprimer</label>'+
                        '<input type="checkbox" name="circtuidetail_set-'+i+'-DELETE" id="id_circtuidetail_set-'+i+'-DELETE">'+
                    '</div>'+
                '</div>'
            );
        });
        $(document).on('click', '.gallery img', function(e) {
            var imgsrc = $(this).attr('src');
            imgclikindex = $(this).index();
            $('.lightbox').css({
                'display':'inline'
            });
            $('#gallery_lightbox').attr('src',imgsrc);
            var hth =$("#gallery_lightbox").height();
            $('.lightboxcontainer').css("height",hth)
        });
        $("#next").click(function () {
            $("#gallery_lightbox").fadeOut(0);
            if(imgclikindex === $('.gallery img').length-1){
                imgclikindex = 0;
            }else {
                imgclikindex++;
            }
            var nextimg = $('.gallery img').eq(imgclikindex).attr('src');
            $('#gallery_lightbox').attr('src',nextimg);
            $("#gallery_lightbox").fadeIn();
        });
        $("#prev").click(function () {
            $("#gallery_lightbox").fadeOut(0);
            if(imgclikindex === 0){
                imgclikindex = $('.gallery img').length-1;
            }else {
                imgclikindex--;
            }
            var nextimg = $('.gallery img').eq(imgclikindex).attr('src');
            $('#gallery_lightbox').attr('src',nextimg);
            $("#gallery_lightbox").fadeIn();
        });
        $('.close-ico').click(function () {
             $('.lightbox').fadeOut(100)
        });
$(document).on('click', '.formset_row input', function(e) {
        var txtClass = $(this).attr("id");
        myindex = $(this).closest('.formset_row').index();
        $('#'+txtClass).change(function () {
          if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
              $("#image").attr("src", e.target.result);
              $("#modalCrop").modal("show");
            };
            reader.readAsDataURL(this.files[0]);
          }
        });
      });
              /* SCRIPTS TO HANDLE THE CROPPER BOX */
        var $image = $("#image");
        var cropBoxData;
        var canvasData;
        $("#modalCrop").on("shown.bs.modal", function () {
          $image.cropper({
            viewMode: 1,
            aspectRatio: 1/1,
            minCropBoxWidth: 900,
            minCropBoxHeight: 700,
            ready: function () {
              $image.cropper("setCanvasData", canvasData);
              $image.cropper("setCropBoxData", cropBoxData);
            }
          });
        }).on("hidden.bs.modal", function () {
          cropBoxData = $image.cropper("getCropBoxData");
          canvasData = $image.cropper("getCanvasData");
          $image.cropper("destroy");
        });

        // Enable zoom in button
        $(".js-zoom-in").click(function () {
          $image.cropper("zoom", 0.1);
        });

        // Enable zoom out button
        $(".js-zoom-out").click(function () {
          $image.cropper("zoom", -0.1);
        });
        /* SCRIPT TO COLLECT THE DATA AND POST TO THE SERVER */
      $(".js-crop-and-upload").click(function () {
        var cropData = $image.cropper("getData");
        $("#id_imageupload_set-"+myindex+"-x").val(3);
        $("#id_imageupload_set-"+myindex+"-y").val(cropData["y"]);
        $("#id_imageupload_set-"+myindex+"-width").val(cropData["height"]);
        $("#id_imageupload_set-"+myindex+"-height").val(cropData["width"]);
        $('#never').click();
      });
});



