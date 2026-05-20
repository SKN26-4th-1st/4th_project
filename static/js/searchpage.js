(function () {
    "use strict";

    // REFACTOR (유지보수성): 엔트리 파일은 초기화만 담당하고 세부 로직은 search/* 모듈로 분리
    const module = window.LGSearchPage || {};
    if (typeof module.initSearchFilter === "function") {
        module.initSearchFilter();
    }
    if (typeof module.initPagination === "function") {
        module.initPagination();
    }
})();
