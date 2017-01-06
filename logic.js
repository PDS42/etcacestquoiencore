function vaportIt(inputStr) {
	var res = ""
	for(i=0; i<inputStr.length; i++) {
		if(inputStr.charCodeAt(i)  >= 33 && inputStr.charCodeAt(i) <= 270) {
			res += String.fromCharCode(inputStr.charCodeAt(i) + 65248);
		} else if(inputStr.charCodeAt(i) == 32) {
			res += String.fromCharCode(12288);
		}
	}
	return res;
}

var finalResult = "";
$('#go').on('click', function() {
	var args = {
		cancer: $('#nbr_cancer').val()
	}
	finalResult = nathalipsum(args)
	$('#output').text(!$('#aesthetic').is(':checked') ? finalResult : vaportIt(finalResult));
})
$('#aesthetic').on('change', function() {
	if (finalResult != '')
		$('#output').text( !$('#aesthetic').is(':checked') ? finalResult : vaportIt(finalResult));
})

function r(min, max) {
	return Math.floor((Math.random() * max) + min);
}
String.prototype.repeat= function(n){
    n= n || 1;
    return Array(n+1).join(this);
}
function nathalipsum(args) {
	var result = "";
	//Entree de paragraphe
	var randEntry = r(0, source.entries.length)
	var randEnd = r(0, source.end.length)
	result += source.entries[randEntry] + " ";

	var delimiters = ["!", "?", "ETC..."];
	var dLength = delimiters.length;
	//Body
	for (var cancer = args.cancer || 5, nbrDispo = source.body.length; cancer >= 0; cancer--) {
		var hasDelimiter = r(0, 2);
		var currDelimiter = (hasDelimiter ? delimiters[r(0, dLength)] : "");
		var nbDelimiters = currDelimiter != "ETC..." ? r(5, 8) : 1;
		result += source.body[r(0, nbrDispo)] + " " + currDelimiter.repeat(nbDelimiters) + " ";
	}
	result += source.end[randEnd] + " " + currDelimiter.repeat(nbDelimiters)

	//Res
	return result;
}