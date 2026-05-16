# Changelog

## 1.2.0 (2026-05-16)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/itellicoAI/server-sdk-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** api update ([5497c74](https://github.com/itellicoAI/server-sdk-python/commit/5497c747d92fe666cacf6136fbbc5ce9d1656446))
* **api:** api update ([0e51dd9](https://github.com/itellicoAI/server-sdk-python/commit/0e51dd93a77ab9c364c4366cd4aef48bdb66e799))
* **api:** api update ([7734372](https://github.com/itellicoAI/server-sdk-python/commit/7734372d62a748301c69f620ef861fcc78763766))
* **internal/types:** support eagerly validating pydantic iterators ([c26be36](https://github.com/itellicoAI/server-sdk-python/commit/c26be36a2a0f4c0f2fd611052f0459cd12ffe066))
* support setting headers via env ([95716e7](https://github.com/itellicoAI/server-sdk-python/commit/95716e7b72e63ffd7a4cc33d466408a0e18cc3a6))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([1dc033b](https://github.com/itellicoAI/server-sdk-python/commit/1dc033bfcab4ee79feace1be405a3650314e704c))
* use correct field name format for multipart file arrays ([30de1ca](https://github.com/itellicoAI/server-sdk-python/commit/30de1ca3d004b75d616a97b328d56a0933066fb8))


### Chores

* **internal:** more robust bootstrap script ([cd44ef0](https://github.com/itellicoAI/server-sdk-python/commit/cd44ef011e95ea82e804f335ef744bd21df09308))
* **internal:** reformat pyproject.toml ([b2ce92d](https://github.com/itellicoAI/server-sdk-python/commit/b2ce92db4f6edbb88e328c328f6f41f5a2d6f458))

## 1.1.0 (2026-04-21)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/itellicoAI/server-sdk-python/compare/v1.0.0...v1.1.0)

### Features

* **api:** api update ([9315576](https://github.com/itellicoAI/server-sdk-python/commit/93155760c9e4e45e3e2bd46716e3cb04d066a307))
* **api:** api update ([efee2c4](https://github.com/itellicoAI/server-sdk-python/commit/efee2c47f9d14da8f96e153844344902a3f4fe88))
* **api:** api update ([51be607](https://github.com/itellicoAI/server-sdk-python/commit/51be6075dbb5571bbbb9ab18600a6fa2705a6ee6))


### Bug Fixes

* ensure streams are always closed ([33d58e4](https://github.com/itellicoAI/server-sdk-python/commit/33d58e4ccf0d784c8cd3c4ff5b66ba577b1fa692))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([953fdc2](https://github.com/itellicoAI/server-sdk-python/commit/953fdc244d8ee456dd7ba04182bb13995a30e835))
* use async_to_httpx_files in patch method ([6e797fa](https://github.com/itellicoAI/server-sdk-python/commit/6e797fa683e0e04fec012c12f45fc752f244ee35))


### Chores

* add missing docstrings ([9ffd9f7](https://github.com/itellicoAI/server-sdk-python/commit/9ffd9f7c53fcadb270937566228b1af994132985))
* add Python 3.14 classifier and testing ([c6a062e](https://github.com/itellicoAI/server-sdk-python/commit/c6a062e34bfdf2cc97ea5be2d6683b5e417ed867))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([b1746c3](https://github.com/itellicoAI/server-sdk-python/commit/b1746c34f34f77d1ae8f8ed1a313ca8099f4dc89))
* **docs:** use environment variables for authentication in code snippets ([11e5dbc](https://github.com/itellicoAI/server-sdk-python/commit/11e5dbcb511c2e56b1bd339fea27da56d866d2b1))
* **internal:** add `--fix` argument to lint script ([12c07bb](https://github.com/itellicoAI/server-sdk-python/commit/12c07bbf4ac1baf1b5b3bfede0cbadf3e178e19e))
* **internal:** add missing files argument to base client ([b743301](https://github.com/itellicoAI/server-sdk-python/commit/b7433016cd77f2708e0e95d50e302544ee3a0bd9))
* **internal:** codegen related update ([776efd8](https://github.com/itellicoAI/server-sdk-python/commit/776efd8e0189dd55e9edf3d98e3986efb9dce8cc))
* **internal:** codegen related update ([4c5e21f](https://github.com/itellicoAI/server-sdk-python/commit/4c5e21fdb7fcf782aec4d0f8ba51377d3e465ff8))
* **internal:** codegen related update ([a938fae](https://github.com/itellicoAI/server-sdk-python/commit/a938faef9dc047ae8fda4571c69eac340d0a2076))
* **internal:** codegen related update ([5ef36ef](https://github.com/itellicoAI/server-sdk-python/commit/5ef36efe484e41b1bd207437c693e668f70c8ec4))
* speedup initial import ([f0f8082](https://github.com/itellicoAI/server-sdk-python/commit/f0f8082a186f16dfedcac57c953519cf22fc9975))
* update lockfile ([0b71c64](https://github.com/itellicoAI/server-sdk-python/commit/0b71c64ad596f87510e6094880699c9afdec8660))

## 1.0.0 (2025-11-12)

Full Changelog: [v0.0.1...v1.0.0](https://github.com/itellicoAI/server-sdk-python/compare/v0.0.1...v1.0.0)

### Features

* **api:** api update ([2f39067](https://github.com/itellicoAI/server-sdk-python/commit/2f39067570924cd5cc4ee08bac38396cba485a8e))
* **api:** api update ([8d9c52a](https://github.com/itellicoAI/server-sdk-python/commit/8d9c52a8277d4244bbf81af3b3e3f2685b3bf52c))
* **api:** manual updates ([1480229](https://github.com/itellicoAI/server-sdk-python/commit/1480229c9bd891fd2b991bed6dfbb253261fc0f2))
* **api:** manual updates ([bc82f6b](https://github.com/itellicoAI/server-sdk-python/commit/bc82f6b1935f2bf1d00e510ea923811fca68be4a))
* **api:** manual updates ([c886ac2](https://github.com/itellicoAI/server-sdk-python/commit/c886ac2382051190eba0d16378f1d6ed5965d138))
* improve future compat with pydantic v3 ([96a36c0](https://github.com/itellicoAI/server-sdk-python/commit/96a36c034613ec03811ee5a48852036553d77687))
* **types:** replace List[str] with SequenceNotStr in params ([34dc3f2](https://github.com/itellicoAI/server-sdk-python/commit/34dc3f29f36ba0f1e86129b2a2ed9ccd026a9114))


### Bug Fixes

* avoid newer type syntax ([54d4ee3](https://github.com/itellicoAI/server-sdk-python/commit/54d4ee3e822ab7bdb11853a0b3b388edcc840478))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([994578b](https://github.com/itellicoAI/server-sdk-python/commit/994578bc1886c6333e41122797da215323240394))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([5496ab6](https://github.com/itellicoAI/server-sdk-python/commit/5496ab64151d19bcc3b1a55abfd7d849cf698ae8))
* **internal:** add Sequence related utils ([5b9a71b](https://github.com/itellicoAI/server-sdk-python/commit/5b9a71b85bc45f652f30cb8fb6ff09f3be478269))
* **internal:** change ci workflow machines ([7351c6a](https://github.com/itellicoAI/server-sdk-python/commit/7351c6a8c81ad05495a7c0a753f78643d498ea92))
* **internal:** move mypy configurations to `pyproject.toml` file ([09823d4](https://github.com/itellicoAI/server-sdk-python/commit/09823d4b76ad53d4c0ff316740042399de016f86))
* **internal:** update pydantic dependency ([d97046a](https://github.com/itellicoAI/server-sdk-python/commit/d97046ab7da6de023ccb3f12a282effcb8ff1511))
* **internal:** update pyright exclude list ([445b31f](https://github.com/itellicoAI/server-sdk-python/commit/445b31f938a0f856d6578dc0331be64e7ff0c47a))
* **tests:** simplify `get_platform` test ([4d69259](https://github.com/itellicoAI/server-sdk-python/commit/4d69259f066cc841c7799ee97c59d4c15e4be2a5))
* **types:** change optional parameter type from NotGiven to Omit ([ede1b9e](https://github.com/itellicoAI/server-sdk-python/commit/ede1b9e5687a7cb36a41e552120b7264cd7ec11e))
* update SDK settings ([5ce33b1](https://github.com/itellicoAI/server-sdk-python/commit/5ce33b1e8ee50d8ce61b0127dea9c08b323a7888))
* update SDK settings ([3b38ec5](https://github.com/itellicoAI/server-sdk-python/commit/3b38ec5cf871814fe2b9296fa9aadfb831ba8060))
