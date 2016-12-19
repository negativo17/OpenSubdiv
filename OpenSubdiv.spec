%global         real_version 3_1_0

# Could NOT find CLEW (missing:  CLEW_INCLUDE_DIR CLEW_LIBRARY) 
# Could NOT find OpenCL (missing:  OPENCL_LIBRARIES OPENCL_INCLUDE_DIRS) (Required is at least version "1.1")
# Could NOT find CUDA (missing:  CUDA_TOOLKIT_ROOT_DIR CUDA_NVCC_EXECUTABLE CUDA_INCLUDE_DIRS CUDA_CUDART_LIBRARY) (Required is at least version "4.0")
# Could NOT find PTex (missing:  PTEX_INCLUDE_DIR PTEX_LIBRARY) (Required is at least version "2.0")
# Could NOT find Docutils (missing:  RST2HTML_EXECUTABLE) (Required is at least version "0.9")

Name:           OpenSubdiv
Version:        3.1.0
Release:        1%{?dist}
Summary:        An Open-Source subdivision surface library
License:        ASL 2.0
URL:            http://graphics.pixar.com/opensubdiv

Source0:        https://github.com/PixarAnimationStudios/%{name}/archive/v%{real_version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 2.8
BuildRequires:  doxygen
BuildRequires:  gcc >= 4.8
BuildRequires:  glew-devel
BuildRequires:  glfw-devel
BuildRequires:  opencl-headers
BuildRequires:  tbb-devel

%description
%{name} is a set of open source libraries that implement high performance
subdivision surface (subdiv) evaluation on massively parallel CPU and GPU
architectures. This code path is optimized for drawing deforming surfaces with
static topology at interactive framerates.

%package        tools
Summary:        Core %{name} tools

%description    tools
OpenSubdiv is a set of open source libraries that implement high performance
subdivision surface (subdiv) evaluation on massively parallel CPU and GPU
architectures. This code path is optimized for drawing deforming surfaces with
static topology at interactive framerates.

%{name} standalone viewers that demonstrate various aspects of the software.

%package        libs
Summary:        Core %{name} libraries

%description    libs
OpenSubdiv is a set of open source libraries that implement high performance
subdivision surface (subdiv) evaluation on massively parallel CPU and GPU
architectures. This code path is optimized for drawing deforming surfaces with
static topology at interactive framerates.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-%{real_version}

%build
%cmake \
    -DCMAKE_LIBDIR_BASE=%{_lib} 
%make_build

%install
%make_install

find %{buildroot} -name "*.a" -delete

# Let the files section pick up the docs
rm -fr %{buildroot}%{_docdir}/opensubdiv

%files tools
%{_bindir}/*

%files libs
%license LICENSE.txt
%doc README.md NOTICE.txt
%{_libdir}/*.so.*

%files devel
%doc documentation/doxy_html
%{_includedir}/opensubdiv/
%{_libdir}/*.so

%changelog
* Sat Dec  3 2016 Simone Caronni <negativo17@gmail.com> - 3.1.0-1
- First build.
