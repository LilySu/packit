from pathlib import Path
from tests.conftest import mock_spec_download_remote_s
from packit.utils import cwd
    spec_package_section = ""
    for section in spec.spec_content.sections:
        if "%package" in section[0]:
            spec_package_section += "\n".join(section[1])
    spec_package_section = ""
    for section in spec.spec_content.sections:
        if "%package" in section[0]:
            spec_package_section += "\n".join(section[1])


def test_srpm(mock_remote_functionality_sourcegit, api_instance_source_git):
    # TODO: we need a better test case here which will mimic the systemd use case
    sg_path = Path(api_instance_source_git.upstream_local_project.working_dir)
    mock_spec_download_remote_s(sg_path / "fedora")
    with cwd(sg_path):
        api_instance_source_git.create_srpm(upstream_ref="0.1.0")
    assert list(sg_path.glob("beer-0.1.0-1.*.src.rpm"))[0].is_file()