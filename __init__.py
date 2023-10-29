{"payload":{"allShortcutsEnabled":false,"fileTree":{"models":{"items":[{"name":"engine","path":"models/engine","contentType":"directory"},{"name":"__init__.py","path":"models/__init__.py","contentType":"file"},{"name":"amenity.py","path":"models/amenity.py","contentType":"file"},{"name":"base_model.py","path":"models/base_model.py","contentType":"file"},{"name":"city.py","path":"models/city.py","contentType":"file"},{"name":"place.py","path":"models/place.py","contentType":"file"},{"name":"review.py","path":"models/review.py","contentType":"file"},{"name":"state.py","path":"models/state.py","contentType":"file"},{"name":"user.py","path":"models/user.py","contentType":"file"}],"totalCount":9},"":{"items":[{"name":"api","path":"api","contentType":"directory"},{"name":"models","path":"models","contentType":"directory"},{"name":"tests","path":"tests","contentType":"directory"},{"name":"web_flask","path":"web_flask","contentType":"directory"},{"name":"web_static","path":"web_static","contentType":"directory"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"0-setup_web_static.sh","path":"0-setup_web_static.sh","contentType":"file"},{"name":"1-pack_web_static.py","path":"1-pack_web_static.py","contentType":"file"},{"name":"2-do_deploy_web_static.py","path":"2-do_deploy_web_static.py","contentType":"file"},{"name":"3-deploy_web_static.py","path":"3-deploy_web_static.py","contentType":"file"},{"name":"AUTHORS","path":"AUTHORS","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"console.py","path":"console.py","contentType":"file"},{"name":"generate_authors.sh","path":"generate_authors.sh","contentType":"file"},{"name":"setup_mysql_dev.sql","path":"setup_mysql_dev.sql","contentType":"file"},{"name":"setup_mysql_test.sql","path":"setup_mysql_test.sql","contentType":"file"},{"name":"test_get_count.py","path":"test_get_count.py","contentType":"file"}],"totalCount":17}},"fileTreeProcessingTime":5.987392,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":709711608,"defaultBranch":"master","name":"AirBnB_clone_v3","ownerLogin":"Hasbi-sabah","currentUserCanPush":false,"isFork":true,"isEmpty":false,"createdAt":"2023-10-25T08:43:27.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/126143242?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1698241010.0","canEdit":false,"refType":"branch","currentOid":"8010100f8f5602d57e00f99ab4a58ca2313ed0e0"},"path":"models/__init__.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","\"\"\"","initialize the models package","\"\"\"","","from os import getenv","","","storage_t = getenv(\"HBNB_TYPE_STORAGE\")","","if storage_t == \"db\":","    from models.engine.db_storage import DBStorage","    storage = DBStorage()","else:","    from models.engine.file_storage import FileStorage","    storage = FileStorage()","storage.reload()"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-s"}],[{"start":0,"end":29,"cssClass":"pl-s"}],[{"start":0,"end":3,"cssClass":"pl-s"}],[],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":7,"cssClass":"pl-s1"},{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":21,"cssClass":"pl-s1"}],[],[],[{"start":0,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":18,"cssClass":"pl-en"},{"start":19,"end":38,"cssClass":"pl-s"}],[],[{"start":0,"end":2,"cssClass":"pl-k"},{"start":3,"end":12,"cssClass":"pl-s1"},{"start":13,"end":15,"cssClass":"pl-c1"},{"start":16,"end":20,"cssClass":"pl-s"}],[{"start":4,"end":8,"cssClass":"pl-k"},{"start":9,"end":15,"cssClass":"pl-s1"},{"start":16,"end":22,"cssClass":"pl-s1"},{"start":23,"end":33,"cssClass":"pl-s1"},{"start":34,"end":40,"cssClass":"pl-k"},{"start":41,"end":50,"cssClass":"pl-v"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":23,"cssClass":"pl-v"}],[{"start":0,"end":4,"cssClass":"pl-k"}],[{"start":4,"end":8,"cssClass":"pl-k"},{"start":9,"end":15,"cssClass":"pl-s1"},{"start":16,"end":22,"cssClass":"pl-s1"},{"start":23,"end":35,"cssClass":"pl-s1"},{"start":36,"end":42,"cssClass":"pl-k"},{"start":43,"end":54,"cssClass":"pl-v"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":25,"cssClass":"pl-v"}],[{"start":0,"end":7,"cssClass":"pl-s1"},{"start":8,"end":14,"cssClass":"pl-en"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/Hasbi-sabah/AirBnB_clone_v3/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/Hasbi-sabah/AirBnB_clone_v3/security/dependabot","repoSecurityAndAnalysisPath":"/Hasbi-sabah/AirBnB_clone_v3/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"__init__.py","displayUrl":"https://github.com/Hasbi-sabah/AirBnB_clone_v3/blob/master/models/__init__.py?raw=true","headerInfo":{"blobSize":"328 Bytes","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"defef63","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FHasbi-sabah%2FAirBnB_clone_v3%2Fblob%2Fmaster%2Fmodels%2F__init__.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"17","truncatedSloc":"13"},"mode":"executable file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/Hasbi-sabah/AirBnB_clone_v3/discussions/new","newIssuePath":"/Hasbi-sabah/AirBnB_clone_v3/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/Hasbi-sabah/AirBnB_clone_v3/blob/master/models/__init__.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/Hasbi-sabah/AirBnB_clone_v3/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/Hasbi-sabah/AirBnB_clone_v3/raw/master/models/__init__.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"Hasbi-sabah","repoName":"AirBnB_clone_v3","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"storage_t","kind":"constant","identStart":82,"identEnd":91,"extentStart":82,"extentEnd":121,"fullyQualifiedName":"storage_t","identUtf16":{"start":{"lineNumber":8,"utf16Col":0},"end":{"lineNumber":8,"utf16Col":9}},"extentUtf16":{"start":{"lineNumber":8,"utf16Col":0},"end":{"lineNumber":8,"utf16Col":39}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/Hasbi-sabah/AirBnB_clone_v3/branches":{"post":"rTckzSwceBpjpccRWjt44SG3PlEUlc_9Qa1j79UqUkhxkFUfANq545OyNXXsLNOZjusa_F10dGuNYlJ5gEa7SQ"},"/repos/preferences":{"post":"QRqqO9yiaEZQwKYV_k6yfMFUhRVt86fki6Eqtm-oP2p5Q7ZFELwQ9976ebQpAqaifel3xbbu_FEB-hbj4Wj3XA"}}},"title":"AirBnB_clone_v3/models/__init__.py at master · Hasbi-sabah/AirBnB_clone_v3"}