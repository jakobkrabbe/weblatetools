

1. Lista alla moduler som saknar .po filen, kolla_svpo.inhouse.sh
2. skapa listan med kommandot... de moduler som fungerar skapar en pofil med ett visst innehåll, de som inte fungerar en bland opfil.


checkmodule -d tmp_database -m survey_likert_scale,survey_mail,survey_manual_review,survey_report,survey_template,survey_website -e -l critical


3. ta bort tomma med skript, ./remove_empty_po.py
4. redigera med PoEdit,
5. Lägg in po-filerna på sätt modul, ./move_sv_po.py
6. ladda till git med git + rätt T/1234 -kommando för uppgiften. 
