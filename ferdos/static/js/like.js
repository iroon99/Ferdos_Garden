function like(id){
    $.ajax({
        type: "GET",
        url: "/memories/like/",
        data: {
            memory_id:id,
        },
        success: function(res){
            $('#icon_like'+id).removeClass('heart-unliked');
            $('#icon_like'+id).attr('onclick', 'dislike(' + id + ')');
            $('#icon_like'+id).addClass('heart-liked');
        }
    });
}

function dislike(id){
    $.ajax({
        type: "GET",
        url: "/memories/dislike/",
        data: {
            memory_id:id,
        },
        success: function(res){
            $('#icon_like'+id).removeClass('heart-liked');
            $('#icon_like'+id).attr('onclick', 'like(' + id + ')');
            $('#icon_like'+id).addClass('heart-unliked');
        }
    });
}